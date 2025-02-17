from ATM import atm
class bank:
    def __init__(self, Atm = [], password = 1234):
        self.Atm = Atm
        self.password = password
        
    def block_atm(self):
        atm_num_input = input("Enter the atm number which you need to blocked: ")
        if atm_num_input.isdigit():
            for item in self.Atm:
                if item.atm_num==int(atm_num_input):
                    # we need to remove this object
                    self.Atm.remove(item)
            print(f"Atm number :{atm_num_input} has been removed ")
        else:
            print("Invalid atm number")
        
            
    def issue_new_atm(self):
        atm_num_input = input("Enter the new atm number: ")
        if atm_num_input.isdigit():
            if atm_num_input in [A.get_atm_num() for A in self.Atm]:
                print("Atm number already exist")
            else:
                self.Atm.append(atm(atm_num_input))
                print(f"New atm number :{atm_num_input} has been added ")
        else:
            print("Invalid atm number")
            
    def update_atm_num(self):
        atm_num_input = input("Enter the atm number which you need to update: ")
        if atm_num_input.isdigit():
            for atm in self.Atm:
                if atm.get_atm_num() == atm_num_input:
                    new_atm_num = input("Enter the new atm number: ")
                    if new_atm_num.isdigit():
                        atm.set_atm_num(new_atm_num)
                        print(f"Atm number :{atm_num_input} has been updated to {new_atm_num}")
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
        else:
            prints("Invalid atm number")
            
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
        else:
            print("Invalid atm number")
            
    def withdraw(self,customer_atm_number):
        atm1 = self.check_atm_number(customer_atm_number)
        if atm1:
            atm1.withdraw_balance()
        else:
            print("Invalid atm number")
    
    def set_atm_pin(self, customer_atm_number):
        atm1 = self.check_atm_number(customer_atm_number)
        if atm1:
            atm1.generate_pin()
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