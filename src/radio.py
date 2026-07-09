import time

from src.menu import show_stations


def play_station(radio, user_station_list):
    while True:
        print("\033[H\033[2J", end="", flush=True)
        show_stations(user_station_list)
        print("~")
        choice = input("Type the index and press enter [or q for exit]: ").strip()

        if choice == "q":
            print("\nExiting...")
            break

        elif choice.isdigit():
            choice_int = int(choice)

            if 1 <= choice_int <= len(user_station_list):
                selected_station = user_station_list[choice_int - 1]
                url = selected_station.url_resolved
                active_station_name = selected_station.name
                radio.play_stream(url)
                return active_station_name

            else:
                print(f"{choice} is not a valid station, please try again ")
                time.sleep(1.5)

        else:
            print("Please choose a valid number")
            time.sleep(1.5)
