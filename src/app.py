from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from textual.containers import Vertical
from textual.binding import Binding

from src.station_list import StationList
from src.media_player import Media_Player
from src.stations_json_parser import parse_json

class RadioCliApp(App):
    def __init__(self) -> None:
        super().__init__()
        self.radio = Media_Player()
        self.user_station_list = parse_json()

    BINDINGS = [
        ("q", "quit", "quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():

            # Add Status bar next
            yield StationList(self.user_station_list)
        yield Footer()

    def play_station(self, station) -> None:
        self.radio.play_stream(station.url_resolved)

    def action_quit(self) -> None:
        self.exit()

    def on_unmount(self) -> None:
        try:
            self.radio.stop()
        except Exception:
                pass
