from src.menu import show_stations


# List the stations, use a for loop through the my_stations, list by int.
# Ask for the input, choice = the input
# Use the choice to filter by stationuuid and use that to find the URL
# Use mpv play URL
def play_station(radio, user_list):
    show_stations(user_list)
    while True:
        choice = input("Type the index and press enter [or q for exit]: ").strip()

        if choice == "q":
            print("\nExiting...")
            break

        elif choice.isdigit():
            choice_int = int(choice)

            if 1 <= choice_int <= len(user_list):
                selected_station = user_list[choice_int - 1]
                url = selected_station.url_resolved
                name = selected_station.name
                print(f"\nYou chose {name}\n")
                radio.play_stream(url)

            else:
                print("That is not a station, please try again ")

        else:
            print("Please choose a valid number")
