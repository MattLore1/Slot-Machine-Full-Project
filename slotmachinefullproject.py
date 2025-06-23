#slot machine game
import random

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

def play_game():
    balance = 100
    
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
        print("Spinning . . . \n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won 💰{payout}")
        else:
            print("You lost this round")
        
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