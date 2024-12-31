# ระบบ ATM

# ระบบสามารถ login เพื่อเข้าใช้งาน แต่ถ้ายังไม่มีเคยมีบัญชีอยู่ ให้ register ก่อน

# 1. login

# 2. register

#    - มีชื่อ นามสกุล

#    - เลขบัญชี Auto // format (AB-1234567)

#    - เบอร์โทรศัพน์

#    - อีเมล

#    - username

#    - password


# เมื่อ login เข้าไปแล้ว จะมี menu ดังนี้

# 1. Deposit // ฝากเงิน

# 2. Withdraw // ถอนเงิน

# 3. Transfer // โอนเงิน

#    - จะต้องโอนเงินไปยังบัญชีที่มีอยู่ในระบบเท่านั้น

# 4. Deactivate an account // ปิดบัญชี

# 5. Account // แสดงรายละเอียด

#     - ชื่อ

#     - นามสกุล

#     - เลขบัญชี AB-1234567

#     - เบอร์โทร 094-732-7499

#     - อีเมล์

#     - จำนวนเงิน 1,000.00 บาท

# 6. logout


import os
import random
import re
import time
from account import Account


class ATM:

    def __init__(self):
        self.accounts = {}
        self.current_account = None

    def generate_account_number(self):
        # start with AB- and then random 7 digits
        return f"AB-{random.randint(1000000, 9999999)}"

    @staticmethod
    def is_valid_email(email):
        regexEmail = r"^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        return re.match(regexEmail, email)

    @staticmethod
    def is_valid_password(password):
        # Regex for validating a password with at least one uppercase, one lowercase, and one special character
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\W).+$"
        return re.match(regex, password)

    @staticmethod
    def timeout_clear():
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")

    def register(self):
        firstname = input("Enter your firstname: ").strip()
        surname = input("Enter your surname: ").strip()
        phone = input("Enter your phone number: ").strip()
        if not phone.isdigit() or len(phone) != 10:
            print("Invalid phone number. Please try again.")
            self.timeout_clear()
            return
        email = input("Enter your email: ").strip()
        if not self.is_valid_email(email):
            print("Invalid email. Please try again.")
            self.timeout_clear()
            return
        password = input("Enter your password: ").strip()
        if not self.is_valid_password(password) or len(password) < 8:
            print("Invalid password. Please try again.")
            self.timeout_clear()
            return
        account = Account(
            firstname, surname, phone, email, self.generate_account_number(), password
        )
        self.accounts[account.username] = account

        print(
            f"Account created successfully! Your account number is {account.username}"
        )
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")

    def deposit(self):
        if not self.current_account:
            print("No account is logged in.")
            return

        try:
            amount = float(input("Enter the amount you want to deposit: ").strip())
            if amount <= 0:
                print("Deposit amount must be greater than 0.")
                return
            result = self.current_account.deposit(amount)
            print(result)
            self.timeout_clear()
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw(self):
        if not self.current_account:
            print("No account is logged in.")
            return

        try:
            amount = float(input("Enter the amount you want to withdraw: ").strip())
            result = self.current_account.withdraw(amount)
            print(result)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        self.timeout_clear()

    def transfer(self):
        if not self.current_account:
            print("No account is logged in.")
            return

        recipient_account = input("Enter the recipient account number: ").strip()
        if recipient_account not in self.accounts:
            print("Recipient account does not exist.")
            return

        try:
            amount = float(input("Enter the amount you want to transfer: ").strip())
            result = self.current_account.transfer(
                amount, self.accounts[recipient_account]
            )
            print(result)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        self.timeout_clear()

    def deactivate_account(self):
        if not self.current_account:
            print("No account is logged in.")
            return
        del self.accounts[self.current_account.username]
        self.current_account = None
        print("Account deactivated successfully!")
        self.timeout_clear()

    def account_details(self):
        if not self.current_account:
            print("No account is logged in.")
            return
        self.current_account.check_account()
        self.timeout_clear()

    def check_balance(self):
        if not self.current_account:
            print("No account is logged in.")
            return
        print(self.current_account.check_balance())
        self.timeout_clear()

    def logout(self):
        self.current_account = None
        print("Logout successful!")
        self.timeout_clear()
        self.run()

    def menu(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Deactivate an account")
            print("5. Account")
            print("6. Check balance")
            print("7. Logout")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                print("\033c")
                self.deposit()
            elif choice == "2":
                print("\033c")
                self.withdraw()
            elif choice == "3":
                print("\033c")
                self.transfer()
            elif choice == "4":
                print("\033c")
                self.deactivate_account()
            elif choice == "5":
                print("\033c")
                self.account_details()
            elif choice == "6":
                print("\033c")
                self.check_balance()
            elif choice == "7":
                print("\033c")
                self.logout()
            else:
                print("Invalid choice. Please try again.")

    def login(self):
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        for account in self.accounts.values():
            if account.username == username and account.password == password:
                self.current_account = self.accounts[account.username]
                print("Login successful!")
                self.timeout_clear()
                return
        print("Invalid username or password. Please try again.")
        self.timeout_clear()

    def run(self):
        while True:
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                print("\033c")
                self.login()
                if self.current_account:
                    self.menu()
            elif choice == "2":
                print("\033c")
                self.register()
            elif choice == "3":
                print("\033c")
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


atm = ATM()
atm.run()

# ทดสอบโดยเปิด terminal แล้วพิมพ์ python main.py
