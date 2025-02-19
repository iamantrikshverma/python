# ATM and Bank Management System

## Introduction
This is a simple ATM and Bank Management System implemented in Python. It provides functionalities for both **customers** and **bank managers** to manage ATM transactions using text files for data storage.

## Features
### **For Customers:**
- Deposit money into their account
- Withdraw money from their account
- Set or update ATM PIN
- Check account balance

### **For Bank Managers:**
- Issue a new ATM card
- Update ATM numbers
- Block an ATM card
- Check the balance of a specific ATM
- Check total bank balance
- Update manager password

## File Structure
```
📂 ATM-Bank-System
│── atm.py          # ATM class handling customer actions
│── bank.py         # Bank class managing ATM accounts
│── main.py         # Main script to run the program
│── atm.txt         # Stores ATM details (ATM number, PIN, balance)
│── password.txt    # Stores manager's password
```

## How It Works
### **1️⃣ ATM Class (atm.py)**
This class handles customer-related operations:
- `generate_pin()`: Allows customers to create a 4-digit PIN.
- `withdraw_balance()`: Withdraws money after PIN verification.
- `deposit_balance()`: Deposits money into the account.
- `check_balance()`: Displays the current account balance.

### **2️⃣ Bank Class (bank.py)**
The bank manages ATM accounts and data:
- `issue_new_atm()`: Issues a new ATM card and stores it in `atm.txt`.
- `block_atm()`: Blocks an ATM by removing it from the file.
- `update_atm_num()`: Updates an ATM number.
- `check_atm_balance()`: Retrieves the balance of a specific ATM.
- `total_balance_in_bank()`: Computes total money in all accounts.
- `change_password()`: Updates the manager’s password in `password.txt`.

### **3️⃣ Main Script (main.py)**
This script runs the program and provides:
- **Manager Access**: Requires password verification to access bank management options.
- **Customer Access**: Customers enter their ATM number to perform transactions.

## Installation & Usage
### **🔹 Requirements**
- Python 3.x

### **🔹 How to Run the Program**
1. **Clone the repository**
   ```sh
   git clone https://github.com/your-repo/ATM-Bank-System.git
   cd ATM-Bank-System
   ```
2. **Run the main script**
   ```sh
   python main.py
   ```
3. **Follow the on-screen options** to proceed as a customer or manager.

## Example Usage
**Manager Login:**
```
Enter Password: admin123
MANAGER ACCESS GRANTED
Choose an option:
1. Issue a new ATM
2. Block an ATM
3. Check total bank balance
...
```

**Customer Login:**
```
Enter ATM Number: 1001
ATM FOUND
Choose an option:
1. Deposit
2. Withdraw
3. Check Balance
...
```

## Notes
- `atm.txt` is used to store ATM account details.
- `password.txt` stores the manager password.

## Explanation
https://youtu.be/sYDN-Gh4uNc



