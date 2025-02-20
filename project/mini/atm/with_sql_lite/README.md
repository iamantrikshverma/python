# ATM System

This project is a simple ATM system implemented in Python using SQLite for data storage. The system allows for basic ATM operations such as issuing new ATMs, managing ATM accounts, and performing transactions.

## Features

- **Manager Operations**:
  - Issue new ATMs
  - Update ATM numbers
  - Block ATMs
  - Check ATM balance
  - Check total balance in the bank
  - Update manager password

- **Customer Operations**:
  - Deposit funds
  - Withdraw funds
  - Set ATM pin
  - Check balance

## Setup

1. **Database Initialization**: The database (`atm_system.db`) is created automatically when the main script is run. It includes tables for `Accounts` and `Password`.

2. **Default Manager Password**: The default manager password is set to `1`. It can be changed through the manager interface.

## How to Run

1. Run the `main.py` script to start the system.

```bash
python main.py
```

2. Follow the on-screen prompts to interact with the system as a manager or customer.

## Dependencies

- Python 3.x
- SQLite

Ensure you have Python and SQLite installed on your system to run this project.

## Notes

- The system is designed for educational purposes and may not include all security features required for a production environment.
- Make sure to update the manager password after the initial setup to ensure security.
