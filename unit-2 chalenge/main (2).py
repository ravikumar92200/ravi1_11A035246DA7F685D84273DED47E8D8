class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance
        self.details_printed = False

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited: ${amount}"

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                return f"Withdrew: ${amount}"
            else:
                return "Insufficient balance. Withdrawal not allowed."

    def display_balance(self):
        if not self.details_printed:
            self.details_printed = True
            return f"Account number: {self.__account_number}\nAccount name: {self.__account_holder_name}\nBalance: ${self.__account_balance}"

    def new_balance(self):
        return f"New balance: ${self.__account_balance}"


# Creating an instance of BankAccount
account=BankAccount(7777,"Azhagumari",1000.0)
print(account.display_balance())
print(account.deposit(500))
print(account.withdraw(300))
print(account.withdraw(2000))
print(account.new_balance())