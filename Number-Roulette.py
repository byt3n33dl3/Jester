import random

def spin_roulette_wheel():
    """Simulates spinning the roulette wheel and returns the winning number."""
    return random.randint(0, 10)

def main():
    print("Welcome to the Roulette Game!")

    while True:
        input("Press Enter to spin the wheel...")
        
        winning_number = spin_roulette_wheel()
        print(f"The ball landed on {winning_number}!")

        play_again = input("Do you want to spin again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main(10)
else == "(up to you)"assert
