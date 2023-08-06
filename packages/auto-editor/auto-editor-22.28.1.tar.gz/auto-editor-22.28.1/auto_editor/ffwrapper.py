import json
import os.path
import subprocess
import sys
from dataclasses import dataclass
from fractions import Fraction
from platform import system
from re import search
from subprocess import PIPE, Popen
from typing import Any, Dict, List, Optional, Tuple

import ae_ffmpeg

from auto_editor.utils.func import get_stdout
from auto_editor.utils.log import Log

IMG_CODECS = ("png", "mjpeg", "webp")
SUB_EXTS = {"mov_text": "srt", "ass": "ass", "webvtt": "vtt"}


class FFmpeg:
    __slots__ = ("debug", "path", "version")

    def __init__(
        self,
        ff_location: Optional[str] = None,
        my_ffmpeg: bool = False,
        debug: bool = False,
    ) -> None:

        def _set_ff_path(ff_location: Optional[str], my_ffmpeg: bool) -> str:
            if ff_location is not None:
                return ff_location
            if my_ffmpeg:
                return "ffmpeg"

            return ae_ffmpeg.get_path()

        self.debug = debug
        self.path = _set_ff_path(ff_location, my_ffmpeg)
        try:
            _version = get_stdout([self.path, "-version"]).split("\n")[0]
            _version = _version.replace("ffmpeg version", "").strip()
            self.version = _version.split(" ")[0]
        except FileNotFoundError:
            if system() == "Darwin":
                Log().error(
                    "No ffmpeg found, download via homebrew or restore the "
                    "included binary."
                )
            if system() == "Windows":
                Log().error(
                    "No ffmpeg found, download ffmpeg with your favorite package "
                    "manager (ex chocolatey), or restore the included binary."
                )

            Log().error("ffmpeg must be installed and on PATH.")

    def print(self, message: str) -> None:
        if self.debug:
            sys.stderr.write(f"FFmpeg: {message}\n")

    def print_cmd(self, cmd: List[str]) -> None:
        if self.debug:
            sys.stderr.write(f"FFmpeg run: {' '.join(cmd)}\n")

    def run(self, cmd: List[str]) -> None:
        cmd = [self.path, "-y", "-hide_banner"] + cmd
        if not self.debug:
            cmd.extend(["-nostats", "-loglevel", "error"])
        self.print_cmd(cmd)
        subprocess.run(cmd)

    def run_check_errors(
        self,
        cmd: List[str],
        log: Log,
        show_out: bool = False,
        path: Optional[str] = None,
    ) -> None:
        def _run(cmd: List[str]) -> str:
            process = self.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)

            _, stderr = process.communicate()

            if process.stdin is not None:
                process.stdin.close()
            return stderr.decode("utf-8", "replace")

        output = _run(cmd)

        if "Try -allow_sw 1" in output:
            cmd.insert(-1, "-allow_sw")
            cmd.insert(-1, "1")
            output = _run(cmd)

        error_list = [
            r"Unknown encoder '.*'",
            r"-q:v qscale not available for encoder\. Use -b:v bitrate instead\.",
            r"Specified sample rate .* is not supported",
            r'Unable to parse option value ".*"',
            r"Error setting option .* to value .*\.",
            r"Undefined constant or missing '.*' in '.*'",
            r"DLL .* failed to open",
            r"Incompatible pixel format '.*' for codec '[A-Za-z0-9_]*'",
            r"Unrecognized option '.*'",
            r"Permission denied",
        ]

        if self.debug:
            print(f"stderr: {output}")

        for item in error_list:
            check = search(item, output)
            if check:
                log.error(check.group())

        if path is not None and not os.path.isfile(path):
            log.error(f"The file {path} was not created.")
        elif show_out and not self.debug:
            print(f"stderr: {output}")

    def Popen(self, cmd: List[str], stdin=None, stdout=PIPE, stderr=None) -> Popen:
        cmd = [self.path] + cmd
        self.print_cmd(cmd)
        return Popen(cmd, stdin=stdin, stdout=stdout, stderr=stderr)

    def pipe(self, cmd: List[str]) -> str:
        cmd = [self.path, "-y"] + cmd

        self.print_cmd(cmd)
        output = get_stdout(cmd)
        self.print(output)
        return output


@dataclass
class VideoStream:
    width: int
    height: int
    codec: str
    fps: float
    time_base: Fraction
    pix_fmt: str
    color_range: Optional[str]
    color_space: Optional[str]
    color_primaries: Optional[str]
    color_transfer: Optional[str]
    bitrate: Optional[str]
    lang: Optional[str]


@dataclass
class AudioStream:
    codec: str
    samplerate: int
    bitrate: Optional[str]
    lang: Optional[str]


@dataclass
class SubtitleStream:
    codec: str
    ext: str
    lang: Optional[str]


class FileInfo:
    __slots__ = (
        "path",
        "abspath",
        "basename",
        "dirname",
        "name",
        "ext",
        "bitrate",
        "description",
        "videos",
        "audios",
        "subtitles",
    )

    def get_res(self) -> Tuple[int, int]:
        if len(self.videos) > 0:
            return self.videos[0].width, self.videos[0].height
        return 1920, 1080

    def get_fps(self) -> float:
        fps = None
        if len(self.videos) > 0:
            fps = self.videos[0].fps

        return 30 if fps is None else fps

    def get_samplerate(self) -> int:
        if len(self.audios) > 0:
            return self.audios[0].samplerate
        return 48000

    def __init__(self, path: str, ffmpeg: FFmpeg, log: Log):
        self.path = path
        self.abspath = os.path.abspath(path)
        self.basename = os.path.basename(path)
        self.dirname = os.path.dirname(os.path.abspath(path))
        self.name, self.ext = os.path.splitext(path)

        self.videos: List[VideoStream] = []
        self.audios: List[AudioStream] = []
        self.subtitles: List[SubtitleStream] = []
        self.description = None

        _dir = os.path.dirname(ffmpeg.path)
        _ext = os.path.splitext(ffmpeg.path)[1]
        ffprobe = os.path.join(_dir, f"ffprobe{_ext}")

        try:
            info = get_stdout(
                [
                    ffprobe,
                    "-v",
                    "-8",
                    "-print_format",
                    "json",
                    "-show_streams",
                    "-show_format",
                    path,
                ]
            )
        except FileNotFoundError:
            log.error(f"Could not find: {ffprobe}")

        def get_attr(name: str, dic: Dict[str, Any], default=-1) -> str:
            if name in dic:
                if isinstance(dic[name], str):
                    return dic[name]
                log.error(f"'{name}' must be a string")
            if default == -1:
                log.error(f"'{name}' must be in ffprobe json")
            if default is not None:
                log.warning(
                    f"'{name}' not found. Using value '{default}' as a placeholder."
                )
            return default

        try:
            json_info = json.loads(info)
            if "streams" not in json_info:
                raise ValueError("Key 'streams' not found")
            if "format" not in json_info:
                raise ValueError("Key 'format' not found")
        except Exception as e:
            log.error(f"{path}: Could not read ffprobe JSON: {e}")

        self.bitrate: Optional[str] = None
        if "bit_rate" in json_info["format"]:
            self.bitrate = json_info["format"]["bit_rate"]
        if (
            "tags" in json_info["format"]
            and "description" in json_info["format"]["tags"]
        ):
            self.description = json_info["format"]["tags"]["description"]

        for stream in json_info["streams"]:
            lang = None
            br = None
            if "tags" in stream and "language" in stream["tags"]:
                lang = stream["tags"]["language"]
            if "bit_rate" in stream:
                br = stream["bit_rate"]

            codec_type = get_attr("codec_type", stream)

            if codec_type in ("video", "audio", "subtitle"):
                codec = get_attr("codec_name", stream)

            if codec_type == "video":
                pix_fmt = get_attr("pix_fmt", stream)
                color_range = get_attr("color_range", stream, default=None)
                color_space = get_attr("color_space", stream, default=None)
                color_primaries = get_attr("color_primaries", stream, default=None)
                color_transfer = get_attr("color_transfer", stream, default=None)
                fps_str = get_attr("avg_frame_rate", stream)
                time_base_str = get_attr("time_base", stream)

                try:
                    fps = float(Fraction(fps_str))
                except ZeroDivisionError:
                    fps = 0
                except ValueError:
                    log.error(f"Could not convert fps '{fps_str}' to float")

                if fps < 1:
                    if codec in IMG_CODECS:
                        fps = 25
                    else:
                        log.error("fps cannot be less than 1.")

                try:
                    time_base = Fraction(time_base_str)
                except (ValueError, ZeroDivisionError):
                    if codec not in IMG_CODECS:
                        log.error(
                            f"Could not convert time_base '{time_base_str}' to Fraction"
                        )
                    time_base = Fraction(0, 1)

                self.videos.append(
                    VideoStream(
                        stream["width"],
                        stream["height"],
                        codec,
                        fps,
                        time_base,
                        pix_fmt,
                        color_range,
                        color_space,
                        color_primaries,
                        color_transfer,
                        br,
                        lang,
                    )
                )
            if codec_type == "audio":
                sr = int(stream["sample_rate"])
                self.audios.append(AudioStream(codec, sr, br, lang))
            if codec_type == "subtitle":
                ext = SUB_EXTS.get(codec, "vtt")
                self.subtitles.append(SubtitleStream(codec, ext, lang))
