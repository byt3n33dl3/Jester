import os
import io
import sys
import random

def display_title():
    title = """
    __         _           _____         _     _   _       
 __|  |___ ___| |_ ___ ___| __  |___ _ _| |___| |_| |_ ___ 
|  |  | -_|_ -|  _| -_|  _|    -| . | | | | -_|  _|  _| -_|
|_____|___|___|_| |___|_| |__|__|___|___|_|___|_| |_| |___|

                    v1 with love - pxcs 
    """
    print(title)

def spin_roulette_wheel():
    """Simulates spinning the roulette wheel and returns the winning number."""
    return random.randint(0, 36)  

def open_failure_files():
    file_names = ["sasser.c", "sasser_remote.c", "sasserftpd.c"]
    for file_name in file_names:
        with open(file_name, "a") as file:
            file.write("Failed to win the roulette game.\n")

def main():
    display_title()
    print("Welcome to the 'J E S T E R R O U L E T T E' Game!")

    while True:
        input("Press Enter to spin the wheel...")

        try:
            winning_number = spin_roulette_wheel()
            print(f"The ball landed on {winning_number}!")

            if winning_number == 7:
                print("You won!")
            else:
                print("You lost! Executing failure files...")
                open_failure_files()

        except Exception as e:
            print(f"An error occurred: {e}")
            open_failure_files()

        play_again = input("Do you want to spin again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
