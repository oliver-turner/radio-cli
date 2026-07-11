from textual.widgets import Static

class Status(Static):
    def __init__(self, **kwargs) -> None:
        startup_message = "Welcome to Radio-CLI :)\nChoose a station and start listening!"
        super().__init__(startup_message, **kwargs)
