import sys


class BankAccount:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance
        print("Account Created Successfully with Number : ", number)

    def deposit(self):
        try:
            amount = float(input("Enter amount to be Deposited: "))
        except ValueError:
            print("Amount entered is invalid")
            return
        if amount <= 0:
            print("Amount to be Deposited must be positive Value")
        else:
            self.balance += amount
            print("Amount Deposited in Account", self.number, "=", amount)
            self.display()

    def display(self):
        print("Available Balance for Account Number", self.number, "=", self.balance)

    def withdraw(self):
        try:
            amount = float(input("Enter amount to be Withdrawn: "))
        except ValueError:
            print("Amount entered is invalid")
            return
        if amount <= 0:
            print("Amount to be Withdrawn must be positive Value")
        else:
            if self.balance >= amount:
                self.balance -= amount
                print("Amount Withdrawn from Account", self.number, "=", amount)
                self.display()
            else:
                print("Insufficient balance in Account", self.number)

    def transfer(self, account):
        try:
            amount = float(input("Enter amount to be transferred: "))
        except ValueError:
            print("Amount entered is invalid")
            return
        if amount <= 0:
            print("Amount to be Transferred must be positive Value")
        else:
            if self.balance >= amount:
                self.balance -= amount
                account.balance += amount
                print("Amount Transferred from Account", self.number, "to Account", account.number, "=", amount)
                self.display()
                account.display()
            else:
                print("Insufficient balance in Account", self.number)


class Main:
    def __init__(self):
        self.accounts = {}

    def operation(self):
        print("Menu Options:")
        print("1. Create Account")
        print("2. Deposit Account")
        print("3. Withdraw Account")
        print("4. Transfer Money")
        print("5. Account Balance")
        print("6. Exit")
        try:
            option = int(input("Enter the option:"))
        except ValueError:
            print("Invalid Choice. Try again")
            return True

        if option == 1:
            try:
                number = int(input("Enter the Account Number:"))
            except ValueError:
                print("Account Number Entered is Invalid")
                return True
            if number <= 0:
                print("Account Number Entered is Invalid")
                return True
            a = self.accounts.get(number)
            if a is None:
                a = BankAccount(number, 0)
                self.accounts[number] = a
            else:
                print("Account already exist with Account Number :", number)
            return True
        elif option == 2:
            try:
                number = int(input("Enter the Account Number:"))
            except ValueError:
                print("Account Number Entered is Invalid")
                return True
            a = self.accounts.get(number)
            if a is None:
                print("The Account does not exist for Account Number:", number)
            else:
                a.deposit()
            return True
        elif option == 3:
            try:
                number = int(input("Enter the Account Number:"))
            except ValueError:
                print("Account Number Entered is Invalid")
                return True
            a = self.accounts.get(number)
            if a is None:
                print("The Account does not exist for Account Number:", number)
            else:
                a.withdraw()
            return True
        elif option == 4:
            try:
                number = int(input("Enter From Account Number:"))
            except ValueError:
                print("Account Number Entered is Invalid")
                return True
            a = self.accounts.get(number)
            if a is None:
                print("The Account does not exist for Account Number:", number)
                return True
            try:
                number1 = int(input("Enter To Account Number:"))
            except ValueError:
                print("Account Number Entered is Invalid")
                return True
            if number1 == number:
                print("To Account Number cannot be same as From AccountNumber")
                return True
            a1 = self.accounts.get(number1)
            if a1 is None:
                print("The Account does not exist for Account Number:", number1)
                return True
            a.transfer(a1)
            return True
        elif option == 5:
            try:
                number = int(input("Enter the Account Number:"))
            except ValueError:
                print("Account Number Entered is Invalid")
                return True
            a = self.accounts.get(number)
            if a is None:
                print("The Account does not exist for Account Number:", number)
            else:
                a.display()
            return True
        elif option == 6:
            return False
        else:
            print("Invalid Choice. Try again")
            return True

    def start(self):
        self.flag = True
        while self.flag:
            self.flag = self.operation()
            print(" ")


m = Main()
m.start()
