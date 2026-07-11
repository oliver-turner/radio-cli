import random
from src.app import RadioCli
from src.constants import ascii_kobes

# Need to move to it's own textual component file
def print_kobe():
    while True:
        random_art = random.choice(ascii_kobes)
        print(random_art)
        back_to_menu = input("Exit [q] ").strip()
        if back_to_menu == "q":
            return
        else:
            print("Not an option, please try again")


if __name__ == "__main__":
    RadioCli().run()
