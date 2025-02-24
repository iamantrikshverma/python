from cryptography.fernet import Fernet
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class atm:
    def __init__(self, atm_num=1, atm_pin=None, account_balance=0, fernet=None):
        self.atm_num = atm_num
        self.atm_pin = None
        self.fernet = fernet if fernet else Fernet(Fernet.generate_key())
        if atm_pin is not None:
            if isinstance(atm_pin, bytes):  # If PIN is already encrypted (from DB)
                self.atm_pin = atm_pin
                logger.debug(f"Loaded encrypted PIN for ATM {self.atm_num}")
            else:  # If PIN is plaintext (newly set)
                self.set_encrypted_pin(atm_pin)
        self.account_balance = float(account_balance)
        
    def generate_pin(self, pin):
        if not pin.isdigit() or len(pin) != 4:
            logger.warning("Invalid PIN format")
            return False
        self.set_encrypted_pin(pin)
        return True
    
    def set_encrypted_pin(self, pin):
        try:
            # Ensure pin is a string and encode it to bytes
            if not isinstance(pin, str):
                pin = str(pin)
            self.atm_pin = self.fernet.encrypt(pin.encode('utf-8'))
            logger.debug(f"Encrypted PIN set for ATM {self.atm_num}")
        except Exception as e:
            logger.error(f"Failed to encrypt PIN: {str(e)}")
            raise
    
    def check_pin(self, pin):
        if self.atm_pin is None:
            logger.warning(f"No PIN set for ATM {self.atm_num}")
            return False
        try:
            decrypted_pin = self.fernet.decrypt(self.atm_pin).decode('utf-8')
            result = pin == decrypted_pin
            logger.debug(f"Checking PIN for ATM {self.atm_num}: Result={result}")
            return result
        except Exception as e:
            logger.error(f"Failed to decrypt PIN for verification: {str(e)}")
            return False
    
    def get_atm_num(self):
        return self.atm_num
    
    def set_atm_num(self, atm_num):
        self.atm_num = atm_num
    
    def get_atm_balance(self):
        return self.account_balance
    
    def get_atm_pin(self):
        return self.atm_pin
    
    def set_atm_balance(self, balance):
        self.account_balance = float(balance)
    
    def __str__(self):
        return f"{self.atm_num},[encrypted_pin],{self.account_balance}"