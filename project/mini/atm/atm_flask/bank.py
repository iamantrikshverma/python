from atm import atm
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

class bank:
    def __init__(self, Atm=[]):
        self.Atm = Atm
        self.client = MongoClient(os.getenv('MONGODB_URI'))
        self.db = self.client['atm_system']
        self.accounts = self.db.accounts
        self.password_collection = self.db.password
        
        encryption_key = os.getenv('ENCRYPTION_KEY')
        if not encryption_key:
            logger.error("ENCRYPTION_KEY not found. Generating a new key.")
            encryption_key = Fernet.generate_key().decode()
            logger.warning(f"Generated ENCRYPTION_KEY: {encryption_key}. Add this to your .env file!")
        try:
            self.fernet = Fernet(encryption_key.encode())
        except Exception as e:
            logger.error(f"Failed to initialize Fernet: {str(e)}")
            raise ValueError("Invalid ENCRYPTION_KEY. Please set a valid Fernet key in .env.")
        
        self.load_atm_data()
        
        pwd = self.password_collection.find_one({'id': 1})
        if not pwd:
            default_password = '1'
            encrypted_pwd = self.fernet.encrypt(default_password.encode('utf-8'))
            self.password_collection.insert_one({'id': 1, 'password': encrypted_pwd})
            self.password = encrypted_pwd
            logger.info("Initialized default password with encryption")
        else:
            self.password = pwd['password']
            logger.debug("Loaded stored encrypted password")

    def encrypt_field(self, value):
        try:
            return self.fernet.encrypt(str(value).encode('utf-8')).decode()
        except Exception as e:
            logger.error(f"Encryption failed: {str(e)}")
            raise

    def decrypt_field(self, encrypted_value):
        if encrypted_value:
            try:
                return self.fernet.decrypt(encrypted_value).decode('utf-8')
            except Exception as e:
                logger.error(f"Decryption failed: {str(e)}")
                return None
        return None

    def load_atm_data(self):
        self.Atm.clear()
        for account in self.accounts.find():
            decrypted_atm_num = self.decrypt_field(account.get('account_number'))
            if decrypted_atm_num is None:
                logger.error(f"Failed to decrypt account_number for document: {account}")
                continue
            decrypted_balance = self.decrypt_field(account.get('balance', None))
            if decrypted_balance is None:
                logger.error(f"Failed to decrypt balance for account_number [REDACTED]")
                decrypted_balance = "0.0"
            atm_obj = atm(
                decrypted_atm_num,
                account.get('pin'),  # Pass encrypted PIN as bytes
                float(decrypted_balance),
                self.fernet
            )
            self.Atm.append(atm_obj)

    def save_atm(self, atm_obj):
        self.accounts.update_one(
            {'account_number': self.encrypt_field(atm_obj.get_atm_num())},
            {
                '$set': {
                    'pin': atm_obj.get_atm_pin(),  # Store encrypted PIN as bytes
                    'balance': self.encrypt_field(atm_obj.get_atm_balance())
                }
            },
            upsert=True
        )

    def issue_new_atm(self, atm_num):
        if not atm_num.isdigit() or atm_num in [a.get_atm_num() for a in self.Atm]:
            logger.warning("Invalid or duplicate ATM number")
            return False
        new_atm = atm(atm_num, fernet=self.fernet)
        self.Atm.append(new_atm)
        self.save_atm(new_atm)
        logger.info("Issued new ATM")
        return True

    def update_atm_num(self, old_num, new_num):
        if not new_num.isdigit() or new_num in [a.get_atm_num() for a in self.Atm]:
            logger.warning("Invalid or duplicate new ATM number")
            return False
        for atm_obj in self.Atm:
            if atm_obj.get_atm_num() == old_num:
                self.accounts.delete_one({'account_number': self.encrypt_field(old_num)})
                atm_obj.set_atm_num(new_num)
                self.save_atm(atm_obj)
                logger.info("Updated ATM number")
                return True
        logger.warning("ATM not found for update")
        return False

    def block_atm(self, atm_num):
        for atm_obj in self.Atm:
            if atm_obj.get_atm_num() == atm_num:
                self.Atm.remove(atm_obj)
                self.accounts.delete_one({'account_number': self.encrypt_field(atm_num)})
                logger.info("Blocked ATM")
                return True
        logger.warning("ATM not found for blocking")
        return False

    def check_atm_balance(self, atm_num):
        for atm_obj in self.Atm:
            if atm_obj.get_atm_num() == atm_num:
                return atm_obj.get_atm_balance()
        logger.warning("ATM not found for balance check")
        return None

    def total_balance_in_bank(self):
        total = sum(atm_obj.get_atm_balance() for atm_obj in self.Atm)
        logger.debug(f"Total balance in bank: {total}")
        return total

    def check_atm_number(self, customer_atm_number):
        for atm in self.Atm:
            if atm.get_atm_num() == customer_atm_number:
                logger.debug("Found ATM")
                return atm
        logger.debug("No ATM found")
        return None

    def deposit(self, atm_number, amount):
        atm_obj = self.check_atm_number(atm_number)
        if atm_obj:
            atm_obj.set_atm_balance(atm_obj.get_atm_balance() + amount)
            self.save_atm(atm_obj)
            logger.info(f"Deposited {amount} to ATM")
            return True
        return False

    def withdraw(self, atm_number, amount):
        atm_obj = self.check_atm_number(atm_number)
        if atm_obj and atm_obj.get_atm_balance() >= amount:
            atm_obj.set_atm_balance(atm_obj.get_atm_balance() - amount)
            self.save_atm(atm_obj)
            logger.info(f"Withdrew {amount} from ATM")
            return True
        logger.warning("Withdrawal failed: insufficient balance or not found")
        return False

    def set_atm_pin(self, atm_number):
        from flask import request
        atm_obj = self.check_atm_number(atm_number)
        if atm_obj:
            pin = request.form['new_pin']
            if atm_obj.generate_pin(pin):
                self.save_atm(atm_obj)
                logger.info("PIN set for ATM")
                return True
        logger.warning("Failed to set PIN for ATM")
        return False

    def change_password(self, new_password):
        encrypted_pwd = self.fernet.encrypt(new_password.encode('utf-8'))
        self.password_collection.update_one(
            {'id': 1},
            {'$set': {'password': encrypted_pwd}},
            upsert=True
        )
        self.password = encrypted_pwd
        logger.info("Manager password updated with encryption")
        return True

    def check_password(self, password):
        logger.debug("Attempting to verify password: [REDACTED]")
        logger.debug(f"Stored encrypted password: {self.password}")
        try:
            decrypted_pwd = self.decrypt_field(self.password)
            if decrypted_pwd is None:
                logger.error("Failed to decrypt stored password")
                return False
            result = password == decrypted_pwd
            logger.debug(f"Password verification result: {result}")
            return result
        except Exception as e:
            logger.error(f"Error verifying password: {str(e)}")
            return False

    def __del__(self):
        self.client.close()