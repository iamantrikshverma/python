from ATM import atm
import os
class bank:
    def __init__(self, Atm = []):
        self.Atm = []
        self.load_atm_file()
        with open("password.txt", "r") as f:
            self.password = f.read().strip() 
            # print(self.password)
        
    def save_atm_file(self):
        with open("atm.txt", "w") as f:
            for atm in self.Atm:
                f.write(atm.__str__() + "\n")
                
            
    def block_atm(self):
        flag = 1
        atm_num_input = input("Enter the atm number which you need to blocked: ")
        # load from file
        for atm in self.Atm:
            if atm.get_atm_num() == atm_num_input: #remove atm
                self.Atm.remove(atm)
                self.save_atm_file()
                print("ATM has been blocked")  
                flag = 0
                break
        if flag:
            print("ATM not found")

    def issue_new_atm(self):
        atm_num_input = input("Enter the new atm number: ")
        if atm_num_input.isdigit():
            if atm_num_input in [A.get_atm_num() for A in self.Atm]:
                print("Atm number already exist")
                print()
            else:
                new_atm = atm(atm_num_input)
                with open("atm.txt", "a") as f:
                    f.write(f"{new_atm.atm_num},{new_atm.get_atm_pin()},{new_atm.get_atm_balance()}")
                    f.write("\n")
                    self.Atm.append(new_atm)
                    print("Added successfully")
                    print()
        else:
            print("Invalid atm number")
    
    
    def load_atm_file(self):
        try:
            with open("atm.txt", "r") as f:
                for line in f:
                    atm_num, pin, balance = line.strip().split(",")
                    try:
                        new_atm = atm(atm_num, pin, float(balance))
                        self.Atm.append(new_atm)
                    except ValueError:
                        print("Bad File")
                        # close the file
                        f.close()
                        # delete this file
                        os.remove("atm.txt")
                        # exit from program
                        exit()
                    # print(f"atm number :{atm_num} has been loaded ")
        except FileNotFoundError:
            print("No atm data file found")
            with open("atm.txt", "w") as file:
                file.write("")
            
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
                        # update in file
                        with open("atm.txt", "r+") as f:
                            # print("hi")
                            lines = f.readlines()
                            # print(lines)
                            i=0
                            for line in lines:
                                atm_num, pin,balance = line.strip().split(",")
                                if atm_num == atm_num_input:
                                    self.Atm[i].set_atm_num(new_atm_num)
                                    lines[i] = f"{new_atm_num},{pin},{balance}\n"
                                    f.seek(0) # rewind
                                    for line in lines:
                                        f.write(line)
                                    f.truncate()
                                    print("Updated successfully")
                                else:
                                    i+=1
                                    
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

    def change_password(self): #update manager password in password.txt
        new_password = input("Enter the new manager password: ")
        with open("password.txt", "w") as f:
            f.write(new_password + "\n")
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
            atm1.deposit_balance()
            with open("atm.txt", "r+") as f:
                lines=f.readlines()
                i=0
                for line in lines:
                    atm_num,pin,_=line.split(',')
                    if atm_num == customer_atm_number:
                        lines[i] = f"{customer_atm_number},{pin},{atm1.get_atm_balance()}\n"
                        f.seek(0) # rewind
                        for line in lines:
                            f.write(line)
                        f.truncate()
                        
                    else:
                        i+=1
            print("Deposit successful")
        else:
            print("Invalid atm number")
            
    def withdraw(self,customer_atm_number):
        atm1 = self.check_atm_number(customer_atm_number)
        if atm1:
            atm1.withdraw_balance()
            with open("atm.txt", "r+") as f:
                lines=f.readlines()
                i=0
                for line in lines:
                    atm_num,pin,_=line.split(',')
                    if atm_num == customer_atm_number:
                        lines[i] = f"{customer_atm_number},{pin},{atm1.get_atm_balance()}\n"
                        f.seek(0) # rewind
                        for line in lines:
                            f.write(line)
                        f.truncate()
                    else:
                        i+=1
            print("withdraw successful")
        else:
            print("Invalid atm number")
    
    def set_atm_pin(self, customer_atm_number):
        atm1 = self.check_atm_number(customer_atm_number)
        if atm1:
            atm1.generate_pin()
            with open("atm.txt", "r+") as f:
                lines=f.readlines()
                i=0
                for line in lines:
                    atm_num,_,balance=line.split(',')
                    if atm_num == customer_atm_number:
                        lines[i] = f"{customer_atm_number},{atm1.get_atm_pin()},{balance}"
                        f.seek(0) # rewind
                        for line in lines:
                            f.write(line)
                        f.truncate()
                    else:
                        i+=1
            print("ATM Pin generated successfully!...")
        else:
            print("Invalid atm number")
    
    def check_atm1_balance(self, customer_atm_number):
        atm1 = self.check_atm_number(customer_atm_number)
        if atm1:
            atm1.check_balance()
        else:
            print("Invalid atm number")
                
    def __str__(self):
        return f"Manager Password is {self.password}"                