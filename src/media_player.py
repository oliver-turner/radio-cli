from winrt.windows.foundation import Uri
from winrt.windows.media.playback import MediaPlaybackState, MediaPlayer


# Need to have name of station in windows + a system tray
class Media_Player:
    STREAM_PLAYING = MediaPlaybackState.PLAYING.value
    STREAM_PAUSED = MediaPlaybackState.PAUSED.value

    def __init__(self):
        self.radio = MediaPlayer()

    def play_stream(self, url_to_play: str):
        clean_url = str(url_to_play).strip()
        uri = Uri(clean_url)
        self.radio.set_uri_source(uri)
        self.radio.play()

    def stop(self):
        if self.is_playing():
            self.radio.pause()
        else:
            print("\nNothing is playing at the moment")

    def start(self):
        if self.is_paused():
            self.radio.play()
        else:
            print("\nUnable to play right now :(")

    def get_status(self):
        return self.radio.playback_session.playback_state

    def is_playing(self) -> bool:
        return self.get_status() == self.STREAM_PLAYING

    def is_paused(self) -> bool:
        return self.get_status() == self.STREAM_PAUSED
