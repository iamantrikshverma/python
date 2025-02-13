from ATM import atm
class user(atm):
    def __init__(self, category,password = '123'):
        self.category = category
        self.password = password
        super().__init__()
        
    def is_manager(self):
        return self.category == 'manager'
    
    def manager_login(self):
        password = input("Enter your password: ")
        if password == self.password:
            print("Welcome, manager!")
            return True
        else:
            print("Incorrect password!")
            return False
        
    def set_atm_num(self):
        if self.is_manager():
            atm_num = input("Enter the ATM number: ")
            self.atm_num = atm_num
            return atm_num
        else:
            print("You are not a manager!")
            return None
        
        
            
        