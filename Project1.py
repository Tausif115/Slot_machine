import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
rows = 3
cols = 3

symbol_count ={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 5
}

def get_slot_machine(rows, cols, symbols):
    all_symbol = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    random.shuffle(all_symbol)

    ans = []
    r = cols
    for i in range(rows):
        ans.append(all_symbol[r-cols:r])
        r+=cols

    return ans


def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number.")
        else:
            print("please enter a valid number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter amount of lines in range.")
        else:
            print("please enter a valid number")
    return lines

def get_bet():
    while True:
        amount = input("Enter the amount you want to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter the bet between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a valid number")
    return amount
   

def cheack_win(slot_machine):
    flag = True
    prev = slot_machine[1][0]
    for i in slot_machine[1]:
        if i!=prev:
            flag = False
    
    if flag:
        print("won the game")
    else:
        print("You loose")
      


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"Sorry, you only have ${balance}, You can't bet ${total_bet}")
        else:
            break    
    print(f"You're betting on {lines} lines with ${bet} on each line. Total bet: ${total_bet}")
    slot_machine = get_slot_machine(rows, cols, symbol_count)

    for i in slot_machine:
        print(" | ".join(i))
    
    cheack_win(slot_machine)


main()


