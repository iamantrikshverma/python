from ATM import atm
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the Accounts table
class Account(Base):
    __tablename__ = 'Accounts'
    account_number = Column(Integer, primary_key=True)
    pin = Column(String(255))
    balance = Column(Float)

# Define the Password table
class Password(Base):
    __tablename__ = 'Password'
    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String(255))

class bank:
    def __init__(self, Atm=[]):
        self.Atm = Atm
        # Connect to the database using SQLAlchemy
        connection_string = 'mysql+pymysql://root:@localhost/atm_system'
        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.load_atm_data()
        self.password = self.session.query(Password).filter_by(id=1).first().password

    def create_tables(self):
        # Tables are created in the __init__ method using Base.metadata.create_all
        pass

    def save_atm_data(self):
        for atm in self.Atm:
            account = self.session.query(Account).filter_by(account_number=atm.get_atm_num()).first()
            if account:
                account.pin = atm.get_atm_pin()
                account.balance = atm.get_atm_balance()
            else:
                new_account = Account(pin=atm.get_atm_pin(), balance=atm.get_atm_balance())
                self.session.add(new_account)
        self.session.commit()

    def block_atm(self):
        flag = 1
        atm_num_input = input("Enter the atm number which you need to block: ")
        for atm in self.Atm:
            if atm.get_atm_num() == atm_num_input:
                self.Atm.remove(atm)
                self.session.query(Account).filter_by(account_number=atm_num_input).delete()
                self.session.commit()
                print("ATM has been blocked")
                flag = 0
                break
        if flag:
            print("ATM not found")

    def issue_new_atm(self):
        atm_num_input = input("Enter the new atm number: ")
        if atm_num_input.isdigit():
            if atm_num_input in [A.get_atm_num() for A in self.Atm]:
                print("Atm number already exists")
                print()
            else:
                new_atm = atm(atm_num_input)
                # No PIN is set initially
                new_account = Account(account_number= int(atm_num_input), pin=None, balance=new_atm.get_atm_balance())
                self.session.add(new_account)
                self.session.commit()
                self.Atm.append(new_atm)
                print("Added successfully")
                print()
        else:
            print("Invalid atm number")

    def load_atm_data(self):
        accounts = self.session.query(Account).all()
        for account in accounts:
            loaded_atm = atm(str(account.account_number), account.pin, account.balance)
            self.Atm.append(loaded_atm)

    def update_atm_num(self):
        atm_num_input = input("Enter the atm number which you need to update: ")
        
        if atm_num_input.isdigit():
            for atm in self.Atm:
                if atm.get_atm_num() == atm_num_input:
                    new_atm_num = input("Enter the new atm number: ")
                    # if new_atm_num already there then no need to update 
                    if new_atm_num.isdigit():
                        if new_atm_num in [A.get_atm_num() for A in self.Atm]:
                            print("Atm number already exist")
                            return
                        # update in database
                        account = self.session.query(Account).filter_by(account_number=atm_num_input).first()
                        account.account_number = new_atm_num
                        atm.set_atm_num(new_atm_num)
                        self.session.commit()
                        print("Updated successfully")
                    else:
                        print("Invalid atm number")
                        break
                    break
        else:
            print("Invalid atm number")

    def check_atm_balance(self):
        flag=1
        atm_num_input = input("Enter the atm number which you need to check balance: ")
        if atm_num_input.isdigit():
            for atm in self.Atm:
                if atm.get_atm_num() == atm_num_input:
                    print(atm.get_atm_balance())
                    flag=0
                    break
        if flag:
            print("ATM Not Found")

    def change_password(self): 
        new_password = input("Enter the new manager password: ")
        password = self.session.query(Password).filter_by(id=1).first()
        password.password = new_password
        self.session.commit()
        self.password = new_password
        print("Manager password has been updated")     

    def total_balance_in_bank(self):
        total_balance = 0
        for atm in self.Atm:
            total_balance += atm.get_atm_balance()
        print(f"Total balance in bank is {total_balance}")

    def check_atm_number(self,customer_atm_number):
        for atm in self.Atm:
            if atm.get_atm_num() == customer_atm_number:
                return atm
        return None

    def deposit(self, customer_atm_number):
        atm1 = self.check_atm_number(customer_atm_number)
        if atm1:
            pin = input("Enter your 4 digit pin: ")
            if pin != str(atm1.get_atm_pin()):
                print("Invalid PIN")
                return
            amount = float(input("Enter amount to deposit: "))
            atm1.set_atm_balance(atm1.get_atm_balance() + amount)
            account = self.session.query(Account).filter_by(account_number=customer_atm_number).first()
            account.balance = atm1.get_atm_balance()
            self.session.commit()
            print("Deposit successful")
        else:
            print("Invalid atm number")

    def withdraw(self,customer_atm_number):
        atm1 = self.check_atm_number(customer_atm_number)
        if atm1:
            pin = input("Enter your 4 digit pin: ")
            if pin != str(atm1.get_atm_pin()):
                print("Invalid PIN")
                return
            amount = float(input("Enter amount to withdraw: "))
            if atm1.get_atm_balance() >= amount:
                atm1.set_atm_balance(atm1.get_atm_balance() - amount)
                account = self.session.query(Account).filter_by(account_number=customer_atm_number).first()
                account.balance = atm1.get_atm_balance()
                self.session.commit()
                print("Withdraw successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid atm number")

    def set_atm_pin(self, customer_atm_number):
        atm1 = self.check_atm_number(customer_atm_number)
        if atm1:
            atm1.generate_pin()
            account = self.session.query(Account).filter_by(account_number=customer_atm_number).first()
            # print(account)
            account.pin = atm1.get_atm_pin()
            self.session.commit()
            print("ATM Pin generated successfully!...")
        else:
            print("Invalid atm number")

    def check_atm1_balance(self, customer_atm_number):
        atm1 = self.check_atm_number(customer_atm_number)
        if atm1:
            pin = input("Enter your 4 digit pin: ")
            if pin != str(atm1.get_atm_pin()):
                print("Invalid PIN")
                return
            print(f"Current balance: {atm1.get_atm_balance()}")
        else:
            print("Invalid atm number")

    def __del__(self):
        if hasattr(self, 'session'):
            self.session.close()

    def __str__(self):
        return f"Manager Password is {self.password}"