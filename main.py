import sys

from src.media_player import Media_Player
from src.menu import show_stations, show_welcome
from src.radio import play_station
from src.stations_json_parser import parse_json


def main():
    radio = Media_Player()
    user_list = parse_json()
    print("\nWelcome to Radio CLI")
    while True:
        show_welcome()
        choice = input("\nEnter your choice and press enter :) ").strip()

        if choice == "1":
            play_station(radio, user_list)
        elif choice == "2":
            show_stations(user_list)
        elif choice == "q":
            print("\nGoodbye :)\n")
            sys.exit()
        else:
            print("\nNot an option, please type either 1, 2 or q")


if __name__ == "__main__":
    main()
