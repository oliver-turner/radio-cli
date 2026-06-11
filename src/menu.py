# Create the terminal interactive menu from here
#
import os

from src.stations_json_parser import parse_json


def interactive_menu():
    tui_width = os.get_terminal_size().columns
    boundary = "=" * tui_width

    my_stations = parse_json()

    print(boundary)
    print(" My Stations ".center(tui_width, "="))
    print()

    for station in my_stations:
        print(
            f"Name: {station.name}\nCountry: {station.country}\n"
            f"Quality: {station.codec} ({station.bitrate}Kpbs)\n"
            f"URL: {station.url_resolved}\n"
        )
    print(boundary)
