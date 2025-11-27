import sys

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_amount(prompt):
    """
    Helper function to handle input validation for amounts.
    It ensures the input is a number and is not negative.
    Returns None if the input is invalid to allow the menu to loop again.
    """
    user_input = input(prompt)
    try:
        amount = float(user_input)
        if amount < 0:
            print("Error: Amount cannot be negative.")
            return None
        return amount
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value (e.g., 50.00).")
        return None

def main():
    cb = Checkbook()
    print("Welcome to the Checkbook Application.")
    
    while True:
        try:
            # .strip() removes leading/trailing whitespace (e.g., " exit " becomes "exit")
            action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

            if action == 'exit':
                print("Exiting program. Goodbye!")
                break

            elif action == 'deposit':
                amount = get_valid_amount("Enter the amount to deposit: $")
                if amount is not None:
                    cb.deposit(amount)

            elif action == 'withdraw':
                amount = get_valid_amount("Enter the amount to withdraw: $")
                if amount is not None:
                    cb.withdraw(amount)

            elif action == 'balance':
                cb.get_balance()

            elif action == '':
                # Handle case where user just presses Enter without typing
                continue 

            else:
                print("Invalid command. Please try again.")

        except KeyboardInterrupt:
            # Handles Ctrl+C gracefully so the program doesn't crash with a traceback
            print("\n\nForce exit detected. Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()
