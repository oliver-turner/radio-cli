import random
import readline
import sys
import time

from src.constants import ascii_kobes
from src.media_player import Media_Player
from src.menu import show_welcome
from src.radio import play_station
from src.stations_json_parser import parse_json


def main():
    radio = Media_Player()
    user_station_list = parse_json()
    active_station_name = "No station is playing"
    try:
        print("\033[?1049h", end="", flush=True)
        while True:
            print("\033[H\033[2J", end="")

            show_welcome(active_station_name)
            choice = input("Type your choice and press enter :) ").strip()

            if choice == "p":
                active_station_name = play_station(radio, user_station_list)
            elif choice == "kobe":
                print_kobe()
            elif choice == "q":
                print("\nGoodbye :)\n")
                sys.exit()
            else:
                print("Not an option, please try again")
                time.sleep(1.5)

    except KeyboardInterrupt:
        print("\nForcing exit. Stopping program")

    finally:
        print("\033[?1049l", end="", flush=True)
        radio.stop()


def print_kobe():
    while True:
        print("\033[H\033[2J", end="")
        random_art = random.choice(ascii_kobes)
        print(random_art)
        back_to_menu = input("Exit [q] ").strip()
        if back_to_menu == "q":
            return
        else:
            print("Not an option, please try again")
            time.sleep(1.5)


if __name__ == "__main__":
    main()
