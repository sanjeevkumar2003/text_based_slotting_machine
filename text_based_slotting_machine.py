import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbols_count ={
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbols_values ={
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

def check_winnings(columns,line,bet,values):
    winnings = 0
    winning_lines = []
    for lines in range(line):
        symbol = columns[0][lines]
        for column in columns:
            symbol_to_check = column[lines]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)
            
    return winnings,winning_lines
             
                
def slotting_machine_spin(rows,cols,symbols_count):
    all_symbols = []
    for symbol, count in symbols_count.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slotting_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end= "|")
            else:
                print(column[row],end = '')

        print()





def deposit():
    while True:
        amount = input("How much amount would you want to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than zero')
        else:
            print('please enter a number')
    return amount


deposit()

def get_number_of_lines():
    while True:
        lines = input(f'How much lines do you want to bet(1-{MAX_LINES})? ')
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print('please enter a valid no of lines')
        else:
            print('please enter a number')
    return lines


get_number_of_lines()

def get_bet():
    while True:
        betting = input('How much amount do you want to bet on each line? $')
        if betting.isdigit():
            betting = int(betting)
            if MIN_BET<=betting<=MAX_BET:
                break
            else:
                print(f'The amount should be in the range of ${MIN_BET} -${MAX_BET}')
        else:
            print('please enter a number')
    return betting


get_bet()

def spin(balance):
     line = get_number_of_lines()
     while True:
        bet = get_bet()
        total_bet = bet*line
        if total_bet > balance:
            print(f'your amount is not sufficient to bet because your current balance is ${balance}')
        else:
            break
     print(f'you are betting ${bet} on {line} so your total bet is ${total_bet}')
     slots = slotting_machine_spin(ROWS,COLS,symbols_count)
     print_slotting_machine(slots)
     winnings,winning_lines = check_winnings(slots,line,bet,symbols_values)
     print(f'you won ${winnings}! ')
     print(f'you won on lines:',*winning_lines)
     return winnings - total_bet
    
def main():
    balance = deposit()
    while True:
        print(f'current balance is ${balance}')
        answer = input('press enter to play(q for quit)')
        if answer == 'q':
            break
        balance += spin(balance)

    print(f'you left with ${balance}')    


main()



   
   

