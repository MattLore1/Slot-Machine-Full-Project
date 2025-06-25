#slot machine game
import random
from playsound import playsound
import threading
import time
import keyboard

cheat_code_buffer = ""
cheat_mode = False

def spin_row(cheat_mode=False):
    symbols = ["🌟","🍒","🍉","🍋","💀"]

    if cheat_mode:
            roll = random.random()
            
            if roll < 0.5:
                lucky_symbol = random.choice(symbols[:3]) # this picks from just the higher pay out symbols
                return [lucky_symbol] * 3
            elif roll < 0.8:
                first = random.choice(symbols) # grantees the first two symbols to match leaving the last to chance
                return [first, first, random.choice()]
            else:
                return [random.choice(symbols) for _ in range(3)] # 20% chance for a non-cheat spin
    
    # normal spin odds
    return [random.choice(symbols) for _ in range (3)]

def print_row(row):
    print("-=-=-=-=-=-=-")
    print(" | ".join(row)) 
    print("-=-=-=-=-=-=-\n")

# sets the payouts per symbol
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

# adds the spin 'animation'
def spin_animation():
    print("\nSpinning", end="", flush=True)

    initial_delay = 1
    time.sleep(initial_delay)

    #sets the speed and slow down of each subsequent dot
    delay = 0.5  
    growth_factor = 1.25

    # prints the 5 dots but one at a time
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(delay)
        delay *= growth_factor

    # this just prints a new line and doesnt need a comment explaining it 
    print("\n")

#looks to turn on cheats with a hidden input
def listen_for_cheat():
    global cheat_code_buffer, cheat_mode
    while True:
        event = keyboard.read_event()
        # this part confused so I cheated with chatgpt - further study required
        if event.event_type == keyboard.KEY_DOWN:
            cheat_code_buffer += event.name
            if len(cheat_code_buffer) > 10:  
                cheat_code_buffer = cheat_code_buffer[-10:]

            # sets the hidden input for cheat mode
            if "lll" in cheat_code_buffer:
                cheat_mode = True

def play_game():
    balance = 100
    playsound("start.mp3")

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(" Welcome to the Python Slot Game!")
    print(" Symbols: 🌟 > 🍒 > 🍉 > 🍋 > 💀")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \n")

    #sets the game play loop and is placed below the "intro" so that if the game is played again it can be skipped
    while balance > 0:
        print(f"current balance: 💰{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        # sets the logic for making bets
        if bet > balance:
            print("insufficient 💰")
            continue

        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet
        print(f"New balance: 💰{balance}")


        # Start spin sound in a separate thread
        spin_sound_thread = threading.Thread(target=play_spin_sound)
        spin_sound_thread.start()

        spin_animation()
        spin_sound_thread.join()

        row = spin_row(cheat_mode)
        print_row(row)

        payout = get_payout(row, bet)

        if payout == (bet * 20):
            print(f"JACKPOT! You won 💰{payout}")
            playsound("big_win.mp3")
        
        elif payout > 0:
            print(f"You won 💰{payout}")
            playsound("win.mp3")

        else:
            print("You lost this round")
            playsound("miss.mp3")
        balance += payout

listener_thread = threading.Thread(target=listen_for_cheat, daemon=True)
listener_thread.start()  

def main():
    while True:
        play_game()
        again = input("Do you want to play again from the beginning? (Y/N): ").upper()
        if again != "Y":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()