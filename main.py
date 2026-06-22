import sys

from src.kobe import print_random_kobe
from src.media_player import Media_Player
from src.menu import show_stations, show_welcome
from src.radio import play_station
from src.stations_json_parser import parse_json


def main():
    radio = Media_Player()
    user_station_list = parse_json()
    active_station_name = "No station is playing"
    print("\nWelcome to Radio CLI")
    while True:
        show_welcome(active_station_name)
        choice = input("\nEnter your choice and press enter :) ").strip()

        if choice == "1":
            active_station_name = play_station(radio, user_station_list)
        elif choice == "2":
            show_stations(user_station_list)
        elif choice == "kobe":
            print_random_kobe()
        elif choice == "q":
            print("\nGoodbye :)\n")
            sys.exit()
        else:
            print("\nNot an option, please type either 1, 2, q, or kobe")


if __name__ == "__main__":
    main()
