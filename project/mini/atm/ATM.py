class atm:
    def __init__(self,atm_num = 1,atm_pin = None,acount_balance = 0):
        self.atm_num = atm_num
        self.atm_pin = atm_pin
        self.acount_balance = acount_balance
        
    def generate_pin(self):
        user_input = input("Enter 4 digits pin: ")
        while not user_input.isdigit():
            user_input = input("Invalid input. Please enter 4 digits pin: ")
    
        while int(user_input) % 10000 != 0:
            user_input = input("Invalid input. Please enter 4 digits pin: ")
        self.atm_pin = user_input
        
    def withdraw_balance(self):
        user_input = input("Enter amount to withdraw: ")
        while not user_input.replace('.', '', 1).isdigit():
            user_input = input("Invalid input. Please enter amount to withdraw: ")
        if user_input > self.acount_balance:
            print("Insufficient balance")
        else:
            self.acount_balance -= float(user_input)
            print("Withdrawal successful")
    
    def deposit_balance(self):
        user_input = input("Enter amount to deposit: ")
        while not user_input.replace('.', '', 1).isdigit():
            user_input = input("Invalid input. Please enter amount to deposit: ")
        self.acount_balance += float(user_input)
        print("Deposit successful")
        
    def check_balance(self):
        print(f"Your current balance is: {self.acount_balance}")
        
    # getter and setters
    
    def get_atm_num(self):
        return self.atm_num
    
    def set_atm_num(self, atm_num):
        self.atm_num = atm_num
        
    # str method
    def __str__(self):
        return f"ATM Number: {self.atm_num}, ATM Pin: {self.atm_pin}"
