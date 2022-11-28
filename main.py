import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Creating a dictionary data structure
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # Looping through every row the user bet on
    for line in range(lines):
        # Reason for using columns 0 index, is because we have all the columns, not all the rows
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            # If the symbol is not equal to the symbol to check, then user did not win
            if symbol != symbol_to_check:
                break
        # This is an else for the for loop, which means that it completed the for loop without breaking. The user won!
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    # easiest way to select a random value is to create a list containing the values and then randomly choosing a value
    all_symbols = []
    # write a for loop that writes whatever symbols into the list
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

# The nested lists represent the values in the column
    columns = []
    for _ in range (cols):
        column = []
        # This is how you COPY a list into another without referencing it
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # select a certain value from list
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def print_slot_machine(columns):
    # Instead of writing out the columns in a list, which makes it seem like rows, we need to transpose them
    for row in range(len(columns[0])):
        # This
        for i, column in enumerate(columns):
            # This is len - 1 because len function checks the maximum element in the list
            if i != len(columns) - 1:
                # this "end" tells the print statement what to end with, as opposed to the default new line character
                print (column[row], end=" | ")
            else:
                print(column[row], end=" ")
        # This empty print statement just prints a new line character when you get to the end of the column, resets the column
        print()

        


# Start with collecting user input
# Amount user will deposit
# Amount user will bet

def deposit():
    # while loop to ask user to deposit valid amount
    while True:
        # input prompts input from the user and allows for text output
        amount = input("What would you like to deposit on each line? $")
        # This is a function that will determine if the variable is a positive whole number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                # if the amount is a valid number, it will break out of the while loop and return amount
                break
            # fail cases
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                # this print method with "f" allows you to put any variable inside that curly braces and it will convert it to a string if it can be converted to a string
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}.")
        else:
            break
        
    print (f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count) 
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    # This is a splat operator, passes every line from list to this print function
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with $ {balance}")
    
            
main()
# Collect bet from user