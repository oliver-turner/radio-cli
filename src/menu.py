# Create the terminal interactive menu from here

from src.stations_json_parser import parse_json

VISUAL_SEPARATOR = "=" * 100


def show_my_stations():

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


# List the stations, use a for loop through the my_stations, list by int.
# Ask for the input, choice = the input
# Use the choice to filter by stationuuid and use that to find the URL
# Use mpv play URL
def play_station():
    my_stations = parse_json()
    print()
    print(VISUAL_SEPARATOR)
    for index, station in enumerate(my_stations, start=1):
        print(index, station.name)
    print(VISUAL_SEPARATOR)

    while True:
        choice = input("Type the index and press enter ").strip()

        if choice.isdigit():
            choice_int = int(choice)

            if 1 <= choice_int <= len(my_stations):
                selected_station = my_stations[choice_int - 1].name
                print(selected_station)

            else:
                print("That is not a station, please try again ")

        else:
            print("Please choose a valid number")
