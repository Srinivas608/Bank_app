class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []

    def view_details(self):
        print(f"Account No: {self.acc_no}\nName: {self.name}\nBalance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print(f"Deposited {amount} successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"Withdrawn {amount} successfully.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def transfer(self, other_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            self.transactions.append(f"Transferred: {amount} to Account {other_account.acc_no}")
            other_account.transactions.append(f"Received: {amount} from Account {self.acc_no}")
            print(f"Transferred {amount} to Account {other_account.acc_no} successfully.")
        else:
            print("Invalid transfer amount or insufficient balance.")

    def print_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, name, initial_deposit=0):
        if acc_no in self.accounts:
            print("Account already exists!")
        else:
            account = Account(acc_no, name, initial_deposit)
            self.accounts[acc_no] = account
            print("Account created successfully.")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no, None)


def main():
    bank = Bank()
    while True:
        print("\nBank App Menu:")
        print("1. Create Account")
        print("2. View Account Details By Accno")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Fund Transfer")
        print("6. Print Transactions")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            acc_no = int(input("Enter Account Number: "))
            name = input("Enter Account Holder Name: ")
            initial_deposit = float(input("Enter Initial Deposit: "))
            bank.create_account(acc_no, name, initial_deposit)
        
        elif choice == 2:
            acc_no = int(input("Enter Account Number: "))
            account = bank.get_account(acc_no)
            if account:
                account.view_details()
            else:
                print("Account not found.")

        elif choice == 3:
            acc_no = int(input("Enter Account Number: "))
            account = bank.get_account(acc_no)
            if account:
                amount = float(input("Enter Amount to Withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")
        
        elif choice == 4:
            acc_no = int(input("Enter Account Number: "))
            account = bank.get_account(acc_no)
            if account:
                amount = float(input("Enter Amount to Deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")
        
        elif choice == 5:
            acc_no_from = int(input("Enter Your Account Number: "))
            account_from = bank.get_account(acc_no_from)
            if account_from:
                acc_no_to = int(input("Enter Recipient Account Number: "))
                account_to = bank.get_account(acc_no_to)
                if account_to:
                    amount = float(input("Enter Amount to Transfer: "))
                    account_from.transfer(account_to, amount)
                else:
                    print("Recipient account not found.")
            else:
                print("Your account not found.")
        
        elif choice == 6:
            acc_no = int(input("Enter Account Number: "))
            account = bank.get_account(acc_no)
            if account:
                account.print_transactions()
            else:
                print("Account not found.")
        
        elif choice == 7:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
