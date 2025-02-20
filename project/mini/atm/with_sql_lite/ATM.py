class atm:
    def __init__(self,atm_num = 1,atm_pin = None,acount_balance = 0):
        self.atm_num = atm_num
        self.atm_pin = atm_pin
        if atm_pin is not None:
            self.atm_pin = int(atm_pin)
        self.acount_balance = acount_balance
        
    def generate_pin(self):
        user_input = input("Enter 4 digits pin: ")
        while not user_input.isdigit():
            user_input = input("Invalid input. Please enter 4 digits pin: ")
    
        while len(user_input) != 4:
            user_input = input("Invalid input. Please enter 4 digits pin: ")
        self.atm_pin = int(user_input)
        
    def withdraw_balance(self):
        pin = input("Enter 4 digit pin: ")
        if not pin.isdigit():
            print("Invalid input.")
            return
        if len(str(pin)) != 4:
            print("Invalid input.")
            return
        if int(pin) != self.atm_pin:
            print("Invalid pin.")
            return
        
        user_input = input("Enter amount to withdraw: ")
        while not user_input.replace('.', '', 1).isdigit():
            user_input = input("Invalid input. Please enter amount to withdraw: ")
        if float(user_input) > self.acount_balance:
            print("Insufficient balance")
        else:
            self.acount_balance -= float(user_input)
            print("Withdrawal successful")
    
    def deposit_balance(self):
        pin = input("Enter 4 digit pin: ")
        if not pin.isdigit():
            print("Invalid input.")
            return
        if len(str(pin)) != 4:
            print("Invalid input.")
            return
        if int(pin) != self.atm_pin:
            print("Invalid pin.")
            return
        
        user_input = input("Enter amount to deposit: ")
        while not user_input.replace('.', '', 1).isdigit():
            user_input = input("Invalid input. Please enter amount to deposit: ")
        self.acount_balance += float(user_input)
        # print("Deposit successful")
        
    def check_balance(self):
        pin = input("Enter 4 digit pin: ")
        if not pin.isdigit():
            print("Invalid input.")
            return
        if len(str(pin)) != 4:
            print("Invalid input.")
            return
        if int(pin) != self.atm_pin:
            print("Invalid pin.")
            return
        
        print(f"Your current balance is: {self.acount_balance}")
        
    # getter and setters 
    
    def get_atm_num(self):
        return self.atm_num
    
    def set_atm_num(self, atm_num):
        self.atm_num = atm_num
    
    def get_atm_balance(self):
        return self.acount_balance
    
    def get_atm_pin(self):
        return self.atm_pin

    def set_atm_balance(self, balance):
        self.acount_balance = balance
    
    # str method
    def __str__(self):
        return f"{self.atm_num},{self.atm_pin},{self.acount_balance}"
