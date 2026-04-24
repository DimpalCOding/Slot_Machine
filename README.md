# Slot_Machine
A simple slot machine project implemented in Python. This project allows users to deposit money, place bets across multiple lines, spin the slot machine, and calculate winnings based on symbol values.

# 🎮 Features

- **Deposit System:** Users can deposit an initial balance before playing.

- **Betting Options:** Choose the number of lines to bet on (up to 5) and set a bet amount per line.

- **Slot Machine Spin:** Randomly generates symbols across 3 rows and 3 columns, with symbol frequency affecting probability.

- **Winning Calculation:** Checks for matching symbols across lines and calculates winnings based on symbol values.

- **Balance Tracking:** Updates balance after each spin, showing winnings or losses.

- **Quit Option:** Exit the game anytime by pressing q.


# 🧩 Symbols and Values

    A → Count: 2, Value: 5

    B → Count: 4, Value: 4

    C → Count: 3, Value: 3

    D → Count: 8, Value: 2

_Symbol frequency determines how often each symbol appears in spins, while symbol value determines payout._

# ⚙️ How It Works

- **_Deposit Balance:_** Enter the amount you want to start with.

- _**Choose Lines:**_ Select how many lines (1–5) you want to bet on.

- _**Place Bet:**_  Enter the bet amount per line (between Rs. 10 and Rs. 100).

- _**Spin the Machine:**_ Press Enter to spin, or q to quit.

- _**View Results:**_ The slot machine displays symbols and calculates winnings.

- _**Balance Update:**_ Your balance is adjusted based on winnings minus total bet.


# 📂 Project Structure

- **SlotMachine.py →** Main game logic and functions.
- **deposit() →** Handles user deposits.
-** get_number_of_line() →** Gets number of lines to bet.
- **get_bet() →** Gets bet amount per line.
- **spin_slot_machine() →** Generates random slot results.
- **print_slot_machine() →** Displays slot machine output.
- **check_winnings() →** Calculates winnings based on results.
- **slotMachineGame() →** Runs a single round of the game.
- **main() →** Entry point for the game loop.

# 📌 Example Gameplay

    What would you like to deposit? Rs. 100

    Enter the number of lines to bet on (1-5)? 3

    What would you like to bet on each line? 20

    You are betting Rs. 20 on 3 lines. Total bet is equal to: Rs. 60

#     Slot Machine Result:
    A | B | D
    A | C | D
    A | B | D

    You won Rs. 100
    Current Balance is Rs. 140

# 💡 Future Improvements

- Add more symbols and paylines.
- Implement graphical interface (GUI).
- Track game history and statistics.
- Add sound effects for spins and wins.

# 👨‍💻 Author

 A beginner friendly Python project to practice loops, functions, and user input handling.
