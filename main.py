import sys

from src.menu import play_station, show_my_stations, show_welcome_menu


def main():
    print("\nWelcome to Radio CLI")
    while True:
        show_welcome_menu()

        choice = input("\nEnter your choice and press enter :) ").strip()

        if choice == "1":
            play_station()
        elif choice == "2":
            show_my_stations()
        elif choice == "q":
            print("\nGoodbye :)\n")
            sys.exit()
        else:
            print("\nNot an option, please type either 1, 2 or q")


if __name__ == "__main__":
    main()
