import time
import sys
from hangman.game import Game
from hangman.interface import Interface
from hangman.player import Player

def main():
    interface = Interface()

    replay = "Y"

    menu_input_flag = 0

    while menu_input_flag == 0:
        interface.clear_screen()
        interface.write_title()
        interface.write_options()
        menu_choice = interface.menu_choice()

        if menu_choice == "1":
            menu_input_flag = 1
            interface.clear_screen()
            while replay == "Y":
                interface.clear_screen()
                player = Player()
                game = Game(player, interface)
                game.start()
                replay = interface.read_replay()

        elif menu_choice == "2":
            interface.clear_screen()
            interface.write_title()
            interface.write_instructions()

        elif menu_choice == "3":
            sys.exit(0)

        else:
            print("Invalid input. Please try again.")
            time.sleep(0.5)
