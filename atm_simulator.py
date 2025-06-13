import sqlite3

# Connect to the SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("atm.db")
cursor = conn.cursor()

# Create accounts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    acc_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    pin TEXT NOT NULL,
    balance REAL DEFAULT 0
)
''')
conn.commit()

# Function to create a new account
def create_account():
    name = input("Enter your name: ")
    pin = input("Choose a 4-digit PIN: ")
    cursor.execute("INSERT INTO accounts (name, pin) VALUES (?, ?)", (name, pin))
    conn.commit()
    
    # Fetch the newly created account number
    acc_no = cursor.lastrowid
    print(f"Account created successfully! Your Account Number is: {acc_no}")


# Function to log in
def login():
    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")
    cursor.execute("SELECT * FROM accounts WHERE acc_no=? AND pin=?", (acc_no, pin))
    account = cursor.fetchone()
    return account

# ATM operations
def atm_menu(account):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance Check\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print(f"Your balance: ₹{account[3]:.2f}")

        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            new_balance = account[3] + amount
            cursor.execute("UPDATE accounts SET balance=? WHERE acc_no=?", (new_balance, account[0]))
            conn.commit()
            account = (account[0], account[1], account[2], new_balance)
            print("Deposit successful!")

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount > account[3]:
                print("Insufficient balance.")
            else:
                new_balance = account[3] - amount
                cursor.execute("UPDATE accounts SET balance=? WHERE acc_no=?", (new_balance, account[0]))
                conn.commit()
                account = (account[0], account[1], account[2], new_balance)
                print("Withdrawal successful!")

        elif choice == '4':
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid option. Try again.")

# Main function
def main():
    while True:
        print("\n=== Welcome to Simple ATM ===")
        print("1. Create Account\n2. Login\n3. Exit")
        option = input("Select an option: ")

        if option == '1':
            create_account()
        elif option == '2':
            user = login()
            if user:
                print(f"\nWelcome, {user[1]}!")
                atm_menu(user)
            else:
                print("Login failed. Invalid account number or PIN.")
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

# Run the program
main()

# Close the database connection
conn.close()
