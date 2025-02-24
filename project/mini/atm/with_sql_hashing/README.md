# ATM System

This project is a simple ATM system implemented in Python using **SQLAlchemy** for database interactions. The system allows for basic ATM operations such as issuing new ATMs, managing ATM accounts, and performing transactions.

## File Structure

The project consists of the following files:

- `ATM.py`: Contains the `atm` class, which defines the properties and methods for ATM operations such as generating PINs and managing account balances.
- `Bank.py`: Contains the `bank` class, which manages the overall bank operations, including database interactions for managing ATM accounts and passwords.
- `main.py`: The main script that initializes the bank system and provides the command-line interface for manager and customer operations.
- `README.md`: This file, providing documentation and setup instructions for the project.

## Features

- **Manager Operations**:
  - **Issue New ATMs**: Allows the manager to create and distribute new ATM cards to customers.
  - **Update ATM Numbers**: Enables the manager to update and manage ATM card numbers in the system.
  - **Block ATMs**: Provides functionality to block ATM cards in case of theft or loss.
  - **Check ATM Balance**: Allows the manager to view the balance of individual ATM accounts.
  - **Check Total Balance in the Bank**: Gives the manager an overview of the total funds available in the bank.
  - **Update Manager Password**: Security feature to change the manager's access password.

- **Customer Operations**:
  - **Deposit Funds**: Customers can deposit money into their ATM accounts.
  - **Withdraw Funds**: Allows customers to withdraw cash from their ATM accounts.
  - **Set ATM Pin**: Security feature for customers to set or change their ATM card PIN.
  - **Check Balance**: Customers can view their current account balance.

## Database Setup

This project uses **SQLAlchemy** to interact with a MySQL database. The connection string is defined in the `main.py` and `Bank.py` files. Ensure you have the following dependencies installed:

```bash
pip install sqlalchemy pymysql
```

### Database Tables

The following tables are created and managed by SQLAlchemy:

- **Accounts**: Stores ATM account information, including account number, PIN, and balance.
- **Password**: Stores the manager's password.

## Code Explanation

- **ATM Class (`ATM.py`)**:
  - **`__init__` Method**: Initializes the ATM object with an ATM number, PIN, and account balance.
  - **`generate_pin` Method**: Allows users to set a 4-digit PIN for their ATM card.
  - **`withdraw_balance` Method**: Handles the withdrawal process, verifying the PIN before allowing cash withdrawal.

- **Bank Class (`Bank.py`)**:
  - **`__init__` Method**: Establishes a connection to the MySQL database using SQLAlchemy and initializes the bank's ATM data.
  - **`create_tables` Method**: Creates the necessary database tables for storing account and password information using SQLAlchemy's ORM.
  - **`save_atm_data` Method**: Saves ATM account data to the database using SQLAlchemy.
  - **`block_atm` Method**: Blocks an ATM card and removes it from the database.

## Setup

1. **Install MySQL**: Ensure you have MySQL installed on your system. You can download it from the [official MySQL website](https://dev.mysql.com/downloads/). Follow the installation instructions provided on the website to set up MySQL on your machine.

2. **Create Database**: Open your MySQL command line or a GUI tool like MySQL Workbench. Log in with your MySQL credentials and create a new database for the ATM system:

   ```sql
   CREATE DATABASE atm_system;
   USE atm_system;
   ```

   This command creates a new database named `atm_system` and sets it as the active database for subsequent operations.

3. **Update Connection Details**: Navigate to the project directory and open the `main.py` and `Bank.py` files. Locate the database connection section in each file and update the following details with your MySQL credentials:

   ```python
   engine = create_engine('mysql+pymysql://yourusername:yourpassword@localhost/atm_system')
   ```

   Replace `yourusername` and `yourpassword` with your actual MySQL username and password.

4. **Install Python Packages**: Ensure Python is installed on your system. Open a terminal or command prompt and install the required Python package:

   ```bash
   pip install sqlalchemy pymysql
   ```

   This command installs the `sqlalchemy` and `pymysql` packages, which are necessary for connecting Python to MySQL using SQLAlchemy.

5. **Run the Application**: With all dependencies installed and the database set up, you can now run the ATM system. Execute the `main.py` script from your terminal or command prompt:

   ```bash
   python main.py
   ```

   The application will start, and you will be prompted to choose between manager and customer operations.

6. **Follow Prompts**: The system provides a command-line interface for interaction. Follow the on-screen prompts to perform various operations as a manager or customer. For example, you can issue new ATMs, deposit funds, or check balances.

## Dependencies

- **Python 3.x**: Ensure you have a compatible version of Python installed.
- **MySQL**: The system uses MySQL for data storage and management.
- **SQLAlchemy**: This package is required for Python to communicate with the MySQL database using SQLAlchemy.
- **PyMySQL**: This package is required for SQLAlchemy to connect to MySQL.

Ensure you have Python and MySQL installed on your system to run this project.

## Default Manager Password

The default manager password is set to `1`. It is recommended to change this password after the initial setup to ensure security.

## Educational Purpose

This system is designed for educational purposes and may not include all security features required for a production environment. It is advisable to enhance security measures if deploying in a real-world scenario.