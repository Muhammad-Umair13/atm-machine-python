class ATM:
    def __init__(self):
        self.Balance = 5000
        self.Pin = 1234


    # Verify if the entered PIN matches the stored PIN
    def check_pin(self, input_pin):
        try:
            if int(input_pin) == self.Pin:
                return True
            else:
                return False
        except ValueError:
            return False


    #  Display the current account balance
    def check_balance(self):
        print(f'''Your Current Balance is: {self.Balance}''')
    
    # Add money to the account
    def deposit(self):
        try:
            depAmount = int(input("Enter amount you want to Deposite: "))
            if depAmount > 0:
                self.Balance += depAmount
                print(f'''Deposited {depAmount}.  New balance: {self.Balance}''')
            else:
                print("Amount must be positive!")
        except ValueError:
            print("Invalid input! Please enter a number.")
            return f"Your Current Balance: {self.Balance}"
    
    # Remove money from the account 
    def withdraw(self):
        try:
            withAmt = int(input("Enter amount you want to Withdraw: "))
            if withAmt <= self.Balance and withAmt > 0 :
                self.Balance -= withAmt
                print(f'''Withdraw Amount: {withAmt}. New balance: {self.Balance}''')
            else:
                print("Enter Correct Amount")
        except ValueError:
            print("Invalid input! Please enter a number.")
            return f"Your Current Balance: {self.Balance}"

    # Terminate the program
    def exit(self):
        print("Thanks For using our ATM, Goodbye!")
        exit()

def main():

    atm = ATM()
    while True:
        pin_input = input("Insert PIN number (or 'q' to quit): ")
        if pin_input.lower() == 'q':
            print(atm.exit())
            
        if atm.check_pin(pin_input):
            print("Correct PIN. Access granted.")
            
            while True:
                print("\n===== ATM Menu =====")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Exit")

                choice = input("Select option (1-4): ")
                if choice == '1':
                    atm.check_balance()
                elif choice == '2':
                    atm.deposit()
                elif choice == '3':
                    atm.withdraw()
                elif choice == '4':
                    atm.exit() 
                else:
                    print("Invalid choice. Please select 1-4")
                break   
            break
        else:
            print("Incorrect PIN. Try again.")
main()