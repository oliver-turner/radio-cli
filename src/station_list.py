from textual.widgets import Label, ListItem, ListView

class StationList(ListView):
    def __init__(self, stations, **kwargs) -> None:
        self._stations = stations
        items = [
            ListItem(
                Label(f"{s.name} — {s.country} — {s.codec} ({s.bitrate}Kbps)")
            )
            for s in stations
        ]
        super().__init__(*items, **kwargs)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        if self.index is not None:
            station = self._stations[self.index]
            self.app.play_station(station)
