class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
            
        elif action.lower() == 'deposit':
            try:
                # Attempt to convert input to a float
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Error: Amount cannot be negative.")
                else:
                    cb.deposit(amount)
            except ValueError:
                # This block runs if the user enters non-numeric data
                print("Invalid input. Please enter a valid number (e.g., 50.00).")
                
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Error: Amount cannot be negative.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                # This block runs if the user enters non-numeric data
                print("Invalid input. Please enter a valid number (e.g., 20.00).")
                
        elif action.lower() == 'balance':
            cb.get_balance()
            
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
