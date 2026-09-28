import random
import json
accounts=[]

def create_account():
    while True:
        try:
            name=input("Enter your name:")
            age=int(input("Enter your age:"))
            if age<=0:
                print("Age should be positive.")
                continue
            print("1.Female")
            print("2.Male")
            print("3.Transgender")
            print("4.Others")  
            print("Select your gender:") 
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
            account=BankAccount(name, age, gender, phone_no,address)
            accounts.append(account)
            print("Account created successfully!")
            print(f"Your Account Number is: {account.account_number}")
            print("Please remember your account number.")
            break
        except ValueError:
            print("Invalid Choice. Try again.")
    save_data()

def create_account_number():
    while True:
        new_account_number=random.randrange(10000,100000)
        is_unique=True
        for account in accounts:
            if account.account_number==new_account_number:
                is_unique=False
        if is_unique:
            return new_account_number


class BankAccount:

    def __init__(self, name, age, gender, phone_no,address, account_number=None):
        self.name = name
        self.balance = 0
        if account_number is not None:
            self.account_number=account_number 
        else:
            self.account_number=create_account_number()
        self.transactions=[]
        self.gender= gender
        self.phone_no= phone_no
        self.age= age
        self.address= address
    def deposit(self,deposit_amount):
        self.balance+=deposit_amount
        print(f"{self.name} deposited ₹{deposit_amount}.")
        self.transactions.append(f"Deposited ₹{deposit_amount}")

    def withdraw(self,withdrawal):
        if withdrawal > self.balance:
            print("Insufficient funds.")
            return
        self.balance-=withdrawal
        print(f"{self.name} has withdrawn {withdrawal}.")
        self.transactions.append(f"Withdrew ₹{withdrawal}")

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def show_balance(self):
        print("The current balance is",self.balance)

    def view_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone_number: {self.phone_no}")
        print(f"Address: {self.address}")
        print(f"Balance: {self.balance}")

def save_data():
    data=[]
    for account in accounts:
        account_dict={}
        account_dict["account_number"]=account.account_number 
        account_dict["name"]=account.name
        account_dict["age"]=account.age
        account_dict["gender"]=account.gender
        account_dict["phone_no"]=account.phone_no
        account_dict["address"]=account.address
        account_dict["balance"]=account.balance
        account_dict["transactions"]=account.transactions
        data.append(account_dict)
    with open("accounts.json",'w') as fh:
        json.dump(data,fh,indent=4)
        

def load_data():
    try:
        with open("accounts.json",'r') as fh:
            data=json.load(fh)
            for account_dict in data:
                account=BankAccount(account_dict["name"],account_dict["age"],account_dict["gender"],account_dict["phone_no"],account_dict["address"],account_dict["account_number"])
                account.account_number=account_dict["account_number"]
                account.balance=account_dict["balance"]
                account.transactions=account_dict["transactions"]
                accounts.append(account)
    except FileNotFoundError:
        print("No existinf data found.")
    except json.JSONDecodeError:
        print("Empty data file.")

                 
def view_account_details():
    account=get_account()
    if account is None:
        return
    else:
        account.view_account_details()

def delete_account():
    account=get_account()
    if account is None:
        return
    else:
        accounts.remove(account)
        print(f"Account {account.account_number} deleted successfully.")
    save_data()


def find_account(account_number):
    for account in accounts:
        if account.account_number==account_number:
            return account
    return None

def get_account():
    try:
        account_number = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number. Try again.")
        return None 
    account = find_account(account_number)

    if account is None:
        print("Account not found.")
        return None 
    return account


def deposit():
    account=get_account()
    if account is None:
        return
    try:
        deposit_amount=int(input("Enter your deposit amount:"))
        if deposit_amount<=0:
            print("Deposit amount should be positive.")
            return 
        else:
            account.deposit(deposit_amount)
    except(ValueError):
        print("Invalid amount. Try again with a valid number.")
    save_data()

def withdraw():
    account=get_account()
    if account is None:
        return
    try:
        withdrawal=int(input("Enter your withdrawal amount:"))
        if withdrawal<=0:
            print("Withdrawal amount needs to be positive.")
            return
        else:
            account.withdraw(withdrawal)
    except(ValueError):
        print("Invalid amount. Try again with a valid number.")
    save_data()

def check_balance():
    account=get_account()
    if account is None:
        return
    else:
        account.show_balance()

def transaction_history():
    account=get_account()
    if account is None:
        return 
    else:
        account.show_transactions()
        
def menu():
    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Account Details")
        print("6. Transaction History")
        print("7. Delete Account")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                create_account()

            elif choice == 2:
                deposit()

            elif choice == 3:
                withdraw()

            elif choice == 4:
                check_balance()

            elif choice == 5:
                view_account_details()

            elif choice == 6:
                transaction_history()

            elif choice == 7:
                delete_account()

            elif choice == 8:
                print("Thank you for using our banking system!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")

load_data()
menu()
