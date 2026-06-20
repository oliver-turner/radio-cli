VISUAL_SEPARATOR = "=" * 100


def show_stations(user_list):
    print()
    print(VISUAL_SEPARATOR)
    print()
    print("My Saved Stations:\n")
    for index, station in enumerate(user_list, start=1):
        print(
            f"{index}: {station.name}\nCountry: {station.country}\n"
            f"Quality: {station.codec} ({station.bitrate}Kpbs)\n",
        )
    print(VISUAL_SEPARATOR)
    return


def show_welcome():
    print("\nMenu")
    print("1. Play")
    print("2. View Saved Stations")
    print("Enter q to exit")
