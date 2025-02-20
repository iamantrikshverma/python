from ATM import atm
import sqlite3
import os

class bank:
    def __init__(self, Atm = []):
        self.Atm = []
        # Connect to the SQLite database
        self.conn = sqlite3.connect('atm_system.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.load_atm_data()
        self.cursor.execute("SELECT password FROM Password WHERE id = 1")
        self.password = self.cursor.fetchone()[0]

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Accounts
            (account_number TEXT PRIMARY KEY, pin TEXT NULL, balance REAL)
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Password
            (id INTEGER PRIMARY KEY, password TEXT)
        ''')
        self.conn.commit()

    def save_atm_data(self):
        self.cursor.executemany("INSERT OR REPLACE INTO Accounts (account_number, pin, balance) VALUES (?, ?, ?)",
                        [(atm.get_atm_num(), atm.get_atm_pin(), atm.get_atm_balance()) for atm in self.Atm])
        self.conn.commit()

    def block_atm(self):
        flag = 1
        atm_num_input = input("Enter the atm number which you need to block: ")
        for atm in self.Atm:
            if atm.get_atm_num() == atm_num_input:
                self.Atm.remove(atm)
                self.cursor.execute("DELETE FROM Accounts WHERE account_number = ?", (atm_num_input,))
                self.conn.commit()
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
                self.cursor.execute("INSERT INTO Accounts (account_number, pin, balance) VALUES (?, ?, ?)",
                                (new_atm.get_atm_num(), None, new_atm.get_atm_balance()))
                self.conn.commit()
                self.Atm.append(new_atm)
                print("Added successfully")
                print()
        else:
            print("Invalid atm number")

    def load_atm_data(self):
        self.cursor.execute("SELECT account_number, pin, balance FROM Accounts")
        rows = self.cursor.fetchall()
        for row in rows:
            loaded_atm = atm(str(row[0]), row[1], row[2])
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
                        self.cursor.execute("UPDATE Accounts SET account_number = ? WHERE account_number = ?", (new_atm_num, atm_num_input))
                        self.conn.commit()
                        atm.set_atm_num(new_atm_num)
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
        self.cursor.execute("UPDATE Password SET password = ? WHERE id = 1", (new_password,))
        self.conn.commit()
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
            self.cursor.execute("UPDATE Accounts SET balance = ? WHERE account_number = ?", (atm1.get_atm_balance(), customer_atm_number))
            self.conn.commit()
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
                self.cursor.execute("UPDATE Accounts SET balance = ? WHERE account_number = ?", (atm1.get_atm_balance(), customer_atm_number))
                self.conn.commit()
                print("Withdraw successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid atm number")

    def set_atm_pin(self, customer_atm_number):
        atm1 = self.check_atm_number(customer_atm_number)
        if atm1:
            atm1.generate_pin()
            self.cursor.execute("UPDATE Accounts SET pin = ? WHERE account_number = ?", (atm1.get_atm_pin(), customer_atm_number))
            self.conn.commit()
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
        self.conn.close()

    def __str__(self):
        return f"Manager Password is {self.password}"