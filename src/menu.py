# Create the terminal interactive menu from here

from src.stations_json_parser import parse_json


def show_my_stations():

    VISUAL_SEPARATOR = "=" * 100

    my_stations = parse_json()
    print()
    print(VISUAL_SEPARATOR)
    print("My Saved Stations:\n")
    for station in my_stations:
        print(
            f"Name: {station.name}\nCountry: {station.country}\n"
            f"Quality: {station.codec} ({station.bitrate}Kpbs)\n"
            f"URL: {station.url_resolved}\n"
        )
    print(VISUAL_SEPARATOR)
    return


def show_welcome_menu():
    print("\nMenu")
    print("1. Play")
    print("2. View Saved Stations")
    print("3. Exit Program")
