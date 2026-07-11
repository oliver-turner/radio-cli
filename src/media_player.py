import subprocess
import sys
from typing import Optional


# Need to have name of station in windows + a system tray
class Win_Media_Player:
    def __init__(self) -> None:
        from winrt.windows.foundation import Uri
        from winrt.windows.media.playback import MediaPlaybackState, MediaPlayer

        self.Uri = Uri
        self.STREAM_PLAYING = MediaPlaybackState.PLAYING.value
        self.STREAM_PAUSED = MediaPlaybackState.PAUSED.value
        self.radio = MediaPlayer()

    def play_stream(self, url_to_play: str):
        clean_url = str(url_to_play).strip()
        uri = self.Uri(clean_url)
        self.radio.set_uri_source(uri)
        self.radio.play()

    def stop(self):
        if self.is_playing():
            self.radio.pause()
            self.radio.close()
        else:
           pass

    def start(self):
        if self.is_paused():
            self.radio.play()
        else:
           pass

    def get_status(self):
        return self.radio.playback_session.playback_state

    def is_playing(self) -> bool:
        return self.get_status() == self.STREAM_PLAYING

    def is_paused(self) -> bool:
        return self.get_status() == self.STREAM_PAUSED

class Linux_Media_Player:
    def __init__(self) -> None:
        self.process: Optional[subprocess.Popen] = None

    def play_stream(self, url_to_play):
        self.stop()
        clean_url = str(url_to_play).strip()
        self.process = subprocess.Popen(
            ["mpv", "--no-video", clean_url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process.wait()  # Clean up the process resource
            self.process = None
        else:
            pass


if sys.platform.startswith("win32"):
    Media_Player = Win_Media_Player
elif sys.platform.startswith("linux"):
    Media_Player = Linux_Media_Player
else:
    supported_os = ["Windows (win32)", "Fedora (Linux)"]
    raise NotImplementedError(
        f"Operating system '{sys.platform}' is not supported. "
        f"This program supports: {', '.join(supported_os)}"
    )
