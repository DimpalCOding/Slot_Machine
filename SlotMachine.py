import random

MAX_LINES = 5
MAX_BET= 100
MIN_BET = 10


ROWS= 3
COLS= 3

symbol_count= {
    "A": 2,
    "B": 4,
    "C": 3,
    "D": 8
}

symbol_value= {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check= column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings +=values[symbol]*bet
    
    return winnings           

#outcome of slot Machine
def spin_slot_machine(rows, cols, symbols):
    #what symbols be in each column based on the frequency of the symbols we have
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            #_(underscore) anamous variable in python where we dont have to care about count or iteration value.
            all_symbols.append(symbol)
            
    columns= []
    for _ in range(cols):
        column = []
        current_symbols= all_symbols[:] #[:] is used to copy the list
        for _ in range(rows):
            value= random.choice(current_symbols) # will be using a copy of all_sumbols so that once the value are used ;get removed so its doesn't get picked again
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(columns)-1:
               print(column[row],  end= " | ")
            else:
                print(column[row], end= "")
                
        print()
                                
def deposit():
    # we made function to collect user input
    while True:
        amount= input("What would you like to deposit? Rs. ")
        # we are asking user to enter the amount, they would to continue to add amount until they give a valid amount
        if amount.isdigit(): #tells us valid number 
           amount = int(amount)
           if amount>0:
               break
           else:
               print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_of_line():
    
    while True:
        lines= input("Enter the number of lines to bet on(1-"+ str(MAX_LINES) + ")? ")
        if lines.isdigit(): #tells us valid number 
           lines = int(lines)
           if 1<= lines <= MAX_LINES:  #to check if the value is betw two values
               break
           else:
               print("Enter valid number of lines.")
        else:
            print("Please enter a number.")     
    return lines

def get_bet(): #basically asking user what they would like to bet on each line
    
    while True:
       amount= input("What would you like to bet on each line?  ")
       if amount.isdigit(): #tells us valid number 
          amount = int(amount)
          if MIN_BET <= amount <= MAX_BET:
              break
          else:
                print(f"Amount must be between Rs. {MIN_BET} - Rs. {MAX_BET} ")
       else:
             print("Please enter a number.")
            
    return amount
 
def slotMachineGame(balance):
       lines = get_number_of_line()
       while True:
          bet = get_bet()
          total_bet = bet* lines
          
          if total_bet > balance:
              print("You don't have enough balanve to bet that amount!")
              print(f"Your current balance is: Rs. {balance}")
          else: 
              break
          
       print(f"You are betting Rs. {bet} on {lines}. Total bet is equal to: Rs. {total_bet}")
        
       slots= spin_slot_machine(ROWS,COLS, symbol_count)
       print_slot_machine(slots)
       winnings= check_winnings(slots, lines, bet, symbol_value)
       print(f"You won Rs. {winnings}")     
 
       return winnings -total_bet
    
def main():
     balance = deposit()  #calling a function
     while True:
         print(f"Current Balance is Rs. {balance}")
         spin =input ("Press enter to spin(q to quit)") 
         if spin =="q":
             break
         balance += slotMachineGame(balance)
     print(f"You left with rs. {balance}")
main()
              
