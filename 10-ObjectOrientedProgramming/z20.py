class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited PLN {amount:.2f} successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew PLN {amount:.2f} successfully."
        else:
            return "Insufficient funds on the account or invalid withdrawal amount."

    def display_info(self):
        return f"Bank Account No: {self.account_number}\nBalance: PLN {self.balance:.2f}"

bank_account = BankAccount("12345655559090111100007722")
print(bank_account.display_info())
print(bank_account.deposit(25.30))
print(bank_account.display_info())
print(bank_account.withdraw(31.70))
print(bank_account.display_info())
print(bank_account.withdraw(14))
print(bank_account.display_info())