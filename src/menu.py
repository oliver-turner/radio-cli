from src.constants import VISUAL_SEPARATOR


def show_stations(user_station_list):
    print("\033[H\033[2J", end="")
    print("My Saved Stations:\n")
    for index, station in enumerate(user_station_list, start=1):
        print(
            f"{index}: {station.name}\nCountry: {station.country}\n"
            f"Quality: {station.codec} ({station.bitrate}Kpbs)\n",
        )
    return


def show_welcome(active_station_name):
    print("Welcome to Radio-CLI")
    print("~")
    print("Menu")
    print(f"Now playing: {active_station_name}")
    print("- Play a Station [p]")
    print("- Exit program [q]")
    print("- Suprise [kobe]")
    print("~")
