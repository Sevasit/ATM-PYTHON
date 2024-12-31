class Account:
    def __init__(
        self, firstname, surname, phone, email, username, password, balance=0.0
    ):
        self.firstname = firstname
        self.surname = surname
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful! New balance: {self.balance:.2f}"
        return "Deposit amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdraw successful! New balance: {self.balance:.2f}"
        return "Withdraw amount must be greater than 0 and less than or equal to your balance."

    def check_balance(self):
        return f"Current balance: {self.balance:.2f}"

    def check_account(self):
        print("----Account details----")
        print(f"Name: {self.firstname} {self.surname}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
        print(f"Account number: {self.username}")
        print(f"Balance: {self.balance:.2f}")
        print("-----------------------")

    def transfer(self, amount, recipient_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient_account.deposit(amount)  # Deposit into the recipient account
            return f"Transfer successful! New balance: {self.balance:.2f}"
        elif amount > self.balance:
            return "Insufficient funds."
        return "Transfer amount must be greater than 0."
