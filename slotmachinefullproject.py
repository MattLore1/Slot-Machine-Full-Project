#slot machine game
import random
from playsound import playsound
import threading
import time

def spin_row():
    symbols = ["🌟","🍒","🍉","🍋","💀"]
    
    return [random.choice(symbols) for _ in range (3)]

def print_row(row):
    print("-=-=-=-=-=-=-")
    print(" | ".join(row)) 
    print("-=-=-=-=-=-=-\n")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🌟':
            return bet * 20
        elif row[0] == '🍒':
            return bet * 10
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 2
        elif row[0] == '💀':
            return bet
    return 0

def play_spin_sound():
    playsound("slot_spin.mp3")

def spin_animation():
    print("Spinning", end="", flush=True)

    initial_delay = 1
    time.sleep(initial_delay)

    delay = 0.5  
    growth_factor = 1.25

    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(delay)
        delay *= growth_factor

    print("\n")

def play_game():
    balance = 100
    playsound("start.mp3")

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(" Welcome to the Python Slot Game!")
    print(" Symbols: 🌟 > 🍒 > 🍉 > 🍋 > 💀")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \n")

    while balance > 0:
        print(f"current balance: 💰{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient 💰")
            continue

        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet
        print(f"New balance: 💰{balance}")

        row = spin_row()

        # Start spin sound in a separate thread
        spin_sound_thread = threading.Thread(target=play_spin_sound)
        spin_sound_thread.start()

        spin_animation()

        spin_sound_thread.join()

        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won 💰{payout}")
            playsound("win.mp3")

        elif payout == (bet * 20):
            print(f"JACKPOT! You won 💰{payout}")
            playsound("big_win.mp3")

        else:
            print("You lost this round")
            playsound("miss.mp3")
        balance += payout
       
def main():
    while True:
        play_game()
        again = input("Do you want to play again from the beginning? (Y/N): ").upper()
        if again != "Y":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()