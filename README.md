#  Simple ATM Transactions (using Python and SQLite)

A terminal-based mini project simulating a basic ATM system using Python and SQLite. Users can create bank accounts, log in using secure PINs, and perform simple transactions such as deposits, withdrawals, and balance checks. Data is stored persistently in a local SQLite database.

---

##  Features

- Create an account with name and 4-digit PIN
- Login using account number and PIN
- Deposit and withdraw funds
- Check account balance
- Data stored permanently using SQLite
- Command-line interface (CLI)

---

##  Tech Stack

- Language: Python3
- Database: SQLite3
- IDE: VS Code (recommended)

---

##  Project Structure

ATM SIMULATOR/
├── atm_simulator.py    # Main program file
├── atm.db              # SQLite database (auto-created on first run)
└── README.md           # Project documentation

---

##  How to Run

1. Clone the repository:
   bash
   git clone git@github.com:khaleedbasha123/Simple-ATM-Transactions.git
   cd Simple-ATM-Transactions
   

2. Run the Python file:
   bash
   python atm.py
   

> On first run, 'atm.db' will be created automatically in your project directory.

---

##  Sample Flow

=== Welcome to Simple ATM ===
1. Create Account
2. Login
3. Exit
Select an option: 1
Enter your name: khaleed
Choose a 4-digit PIN: 1234
Account created successfully! Your Account Number is: 1

=== Welcome to Simple ATM ===
1. Create Account
2. Login
3. Exit
Select an option: 2
Enter Account Number: 1
Enter PIN: 1234

--- ATM Menu ---
1. Balance Check
2. Deposit
3. Withdraw
4. Exit