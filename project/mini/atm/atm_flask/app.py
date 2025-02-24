from flask import Flask, render_template, request, redirect, url_for, flash, session
from bank import bank
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

our_bank = bank()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            logger.debug(f"Form data received: {dict(request.form)}")  # Avoid logging sensitive values directly
            user_type = request.form['user_type']
            login_input = request.form['password']
            logger.debug(f"Login attempt - user_type: {user_type}, input: [REDACTED]")  # Redact password/ATM number

            if user_type == 'manager':
                if our_bank.check_password(login_input):
                    session['user_type'] = 'manager'
                    session.modified = True
                    logger.info("Manager login successful")
                    return redirect(url_for('manager'))
                else:
                    flash('Invalid password')
                    logger.warning("Invalid manager password")
            elif user_type == 'customer':
                atm = our_bank.check_atm_number(login_input)
                if atm:
                    session['user_type'] = 'customer'
                    session['atm_number'] = login_input
                    session.modified = True
                    logger.info(f"Customer login successful for ATM [REDACTED]")
                    return redirect(url_for('customer', atm_number=login_input))
                else:
                    flash('Invalid ATM number')
                    logger.warning("Invalid ATM number")
            else:
                flash('Invalid user type')
                logger.error(f"Unexpected user_type: {user_type}")
        except KeyError as e:
            flash(f"Missing form field: {str(e)}")
            logger.error(f"KeyError in form data: {str(e)}")
            return render_template('login.html'), 400
        except Exception as e:
            flash('An error occurred during login')
            logger.error(f"Login error: {str(e)}")
            return render_template('login.html'), 400
    return render_template('login.html')

@app.route('/manager', methods=['GET', 'POST'])
def manager():
    if 'user_type' not in session or session['user_type'] != 'manager':
        flash('Please login as manager')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        action = request.form['action']
        if action == 'issue_atm':
            atm_num = request.form['atm_number']
            if our_bank.issue_new_atm(atm_num):
                flash('ATM issued successfully')
            else:
                flash('Failed to issue ATM')
        elif action == 'update_atm':
            old_num = request.form['old_number']
            new_num = request.form['new_number']
            if our_bank.update_atm_num(old_num, new_num):
                flash('ATM number updated successfully')
            else:
                flash('Failed to update ATM number')
        elif action == 'block_atm':
            atm_num = request.form['atm_number']
            if our_bank.block_atm(atm_num):
                flash('ATM blocked successfully')
            else:
                flash('ATM not found')
        elif action == 'check_balance':
            atm_num = request.form['atm_number']
            balance = our_bank.check_atm_balance(atm_num)
            if balance is not None:
                flash(f"Balance: {balance}")
            else:
                flash('ATM not found')
        elif action == 'total_balance':
            total = our_bank.total_balance_in_bank()
            flash(f"Total bank balance: {total}")
        elif action == 'update_password':
            new_password = request.form['new_password']
            our_bank.change_password(new_password)
            flash('Password updated successfully')
    return render_template('manager.html')

@app.route('/customer/<atm_number>', methods=['GET', 'POST'])
def customer(atm_number):
    logger.debug(f"Entering customer route with atm_number=[REDACTED]")
    logger.debug(f"Session data: {session}")
    
    if 'user_type' not in session or session['user_type'] != 'customer' or session.get('atm_number') != atm_number:
        flash('Please login as customer')
        logger.warning("Session check failed, redirecting to login")
        return redirect(url_for('login'))
    
    atm = our_bank.check_atm_number(atm_number)
    if not atm:
        flash('Invalid ATM number')
        logger.warning(f"ATM not found for [REDACTED]")
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        logger.debug(f"Customer POST request: {dict(request.form)}")  # Avoid logging PIN directly
        action = request.form['action']
        pin = request.form.get('pin', '')
        
        if action != 'set_pin' and not atm.check_pin(pin):
            flash('Invalid PIN')
            logger.warning("Invalid PIN provided")
            return render_template('customer.html', atm_number=atm_number)
            
        if action == 'deposit':
            amount = float(request.form['amount'])
            if our_bank.deposit(atm_number, amount):
                flash('Deposit successful')
            else:
                flash('Deposit failed')
        elif action == 'withdraw':
            amount = float(request.form['amount'])
            if our_bank.withdraw(atm_number, amount):
                flash('Withdrawal successful')
            else:
                flash('Insufficient balance or withdrawal failed')
        elif action == 'set_pin':
            if our_bank.set_atm_pin(atm_number):
                flash('PIN set successfully')
            else:
                flash('Failed to set PIN')
        elif action == 'check_balance':
            balance = atm.get_atm_balance()
            flash(f"Current balance: {balance}")
    
    logger.debug("Rendering customer.html")
    return render_template('customer.html', atm_number=atm_number)

@app.route('/logout')
def logout():
    session.pop('user_type', None)
    session.pop('atm_number', None)
    flash('Logged out successfully')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)