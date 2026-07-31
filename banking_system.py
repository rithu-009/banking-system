import random
import json
accounts=[]

def create_account():
    account_dictionary={}
    while True:
        try:
            name=input("Enter your name:")
            age=int(input("Enter your age:"))
            if age<0:
                print("Age should be positive.")
                continue
            print("1.Female")
            print("2.Male")
            print("3.Transgender")
            print("4.Others")   
            genders=["Female","Male","Transgender","Others"]
            gender_choice=int(input("Enter your gender choice:"))
            if not (1 <= gender_choice <= len(genders)):
                 print("Invalid Choice. Try Again.")
                 continue
            gender=genders[gender_choice-1]
            phone_no=input("Enter your 10 digit phone number:")
            if len(phone_no)!=10:
                print("Invalid phone number. Try Again.")
                continue
            if not phone_no.isdigit():
                 print("Phone number should contain only digits.")
                 continue
            address=input("Enter your address:")
            account_dictionary["name"]=name
            account_dictionary["age"]=age
            account_dictionary["gender"]=gender
            account_dictionary["phone number"]=phone_no
            account_dictionary["address"]=address
            account_dictionary["account number"]=create_account_number()
            account_dictionary["transactions"]=[]
            account_dictionary["balance"]=0

            accounts.append(account_dictionary)
            break
        except ValueError:
            print("Invalid Choice. Try again.")

def create_account_number():
    while True:
        new_account_number=random.randrange(10000,100000)
        is_unique=True
        for account in accounts:
            if account["account number"]==new_account_number:
                is_unique=False
        if is_unique:
            return new_account_number

class BankAccount:

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.account_number=create_account_number()
        self.transactions=[]

    def deposit(self,deposit_amount):
        self.balance+=deposit_amount
        print(self.name,"has deposited",deposit_amount,".")
        self.transactions.append(f"Deposited ₹{deposit_amount}")

    def withdraw(self,withdrawal):
        if withdrawal > self.balance:
            print("Insufficient funds.")
            return
        self.balance-=withdrawal
        print(self.name,"has withdrawn",withdrawal,".")
        self.transactions.append(f"Withdrew ₹{withdrawal}")

    def show_transactions(self):
        print(self.transactions)

    def show_balance(self):
        print("The current balance is",self.balance)

rithu=BankAccount("Rithu")
rithu.deposit(500)
rithu.withdraw(600)
rithu.show_balance()

def create_account_number():
    while True:
        new_account_number=random.randrange(10000,100000)
        is_unique=True
        for account in accounts:
            if account["account number"]==new_account_number:
                is_unique=False
        if is_unique:
            return new_account_number
                


                



