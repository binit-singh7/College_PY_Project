# 2. Simple ATM Simulation
# Objective: Create a simulation for basic ATM operations.
# Steps:
# 1. Initialize a default balance (e.g., 10,000).
# 2. Provide a menu with options:
# o Check balance.
# o Deposit money.
# o Withdraw money.
# o Exit.
# 3. For deposit, add the entered amount to the balance.
# 4. For withdrawal, ensure the entered amount is less than or equal to the balance.
# 5. Loop the program until the user chooses to exit.

def main():
    balance = 10000
    while True:
        print("\nATM Menu:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(f"Your balance is: {balance}")
        elif choice == "2":
            amount = int(input("Enter the amount to deposit: "))
            balance += amount
            print(f"Deposit successful. Your new balance is: {balance}")
        elif choice == "3":
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successful. Your new balance is: {balance}")
            else:
                print("Insufficient balance.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()            