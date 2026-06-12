import sys

from src.menu import show_my_stations, show_welcome_menu


def main():
    print("\nWelcome to Radio CLI")
    while True:
        show_welcome_menu()

        choice = input("\nType the index and press enter :) ").strip()

        if choice == "1":
            print("\nDo this next")
        elif choice == "2":
            show_my_stations()
        elif choice == "3":
            print("\nGoodbye :)\n")
            sys.exit()
        else:
            print("\nNot an option, please type either 1, 2 or 3")


if __name__ == "__main__":
    main()
