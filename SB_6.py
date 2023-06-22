class BankAccount:

    def __init__(self, accountnumber, name, balance):
        self.accountNumber = accountnumber
        self.name = name
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdrawal(self, withdrawal):
        while self.balance - withdrawal < 0:
            print("Insufficient Balance")
            withdrawal = int(input("Withdrawal: "))
        self.balance -= withdrawal

    def display(self):
        print(f"====================================\nAccount Number: {self.accountNumber}\nAccount Name: {self.name}"
              f"\nAccount Balance: ${self.balance}")


newAccount = BankAccount(1234567890, "Joy", 2700)
wd = input("Withdrawal: ")
newAccount.withdrawal(int(wd))
dep = input("Deposit: ")
newAccount.deposit(int(dep))
newAccount.display()