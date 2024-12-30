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
        email = input("Enter your email: ").strip()
        if not self.is_valid_email(email):
            print("Invalid email. Please try again.")
            self.timeout_clear()
            return
        password = input("Enter your password: ").strip()
        if not self.is_valid_email(email):
            print("Invalid email. Please try again.")
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

    def menu(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Deactivate an account")
            print("5. Account")
            print("6. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.transfer()
            elif choice == "4":
                self.deactivate_account()
            elif choice == "5":
                self.account_details()
            elif choice == "6":
                self.logout()
            else:
                print("Invalid choice. Please try again.")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for account in self.accounts.values():
            if account.username == username and account.password == password:
                self.current_account = account
                print("Login successful!")
                return
        print("Invalid username or password. Please try again.")

    def run(self):
        while True:
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("Enter your choice: ")
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
