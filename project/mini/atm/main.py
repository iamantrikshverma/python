from Bank import bank

our_bank = bank() #global bank object initially empty

def main(our_bank):
    print("Welcome to our_bank!........")
    print()
    while True:
        print("Choose an Option: ")
        print("1. MANAGER ")
        print("2. CUSTOMER")
        print("3. EXIT")
        print()
        choice = input("Enter your choice: ")
        if choice == "1":
            print("MANAGER")
            print()
            manager_password = input("Enter Password: ")
            with open("password.txt", "r") as f:
                password = f.read().strip()
                # print(password)
                # print(manager_password)
            
                if manager_password == password:
                    print("MANAGER ACCESS GRANTED")
                    print()
                    while True:
                        print("Choose an option: ")
                        print("1. Issue a new ATM!")
                        print("2. Update Atm number!")
                        print("3. Delete an ATM!")
                        print("4. Check Balance!")
                        print("5. Check total Balance in Bank!")
                        print("6. Update Manager Password!")
                        print("7. Logout!")
                        print()
                        manager_choice = input("Enter your choice: ")
                        if manager_choice == "1":
                            our_bank.issue_new_atm()
                        elif manager_choice == "2":
                            our_bank.update_atm_num()
                        elif manager_choice == "3":
                            our_bank.block_atm()
                        elif manager_choice == "4":
                            our_bank.check_atm_balance()
                        elif manager_choice == "5":
                            our_bank.total_balance_in_bank()
                        elif manager_choice == "6":
                            our_bank.change_password() 
                        elif manager_choice == "7":
                            print("Logout successfully!")
                            break
                        else:
                            print("Invalid choice!")
                            break
                else:
                    print("Invalid Password!")
        elif choice == "2":
            print("CUSTOMER")
            print()
            customer_atm_number = input("Enter atm number: ")
            if customer_atm_number.isdigit():
                atm =  our_bank.check_atm_number(customer_atm_number)
                if atm:
                    print("ATM FOUND")
                    print()
                    while True:
                        print("Choose an option: ")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Set atm pin")
                        print("4. Check Balance!")
                        print("5. Logout!")
                        print()
                        customer_choice = input("Enter your choice: ")
                        if customer_choice == "1":
                            our_bank.deposit(customer_atm_number)
                        elif customer_choice == "2":
                            our_bank.withdraw(customer_atm_number)
                        elif customer_choice == "3":
                            our_bank.set_atm_pin(customer_atm_number)
                        elif customer_choice == "4":
                            our_bank.check_atm1_balance(customer_atm_number)
                        elif customer_choice == "5":
                            print("Logout successfully!")
                            break
                        else:
                            print("Invalid choice!")
                            break
                else:
                    print("ATM NOT FOUND")
            else:
                print("Invalid atm number!")
        elif choice == "3":
            print("EXITING.....\nThankyou for using our service!..")
            break
        else:
            print("Invalid choice!")
            break
            
if __name__ == "__main__": 
    main(our_bank)