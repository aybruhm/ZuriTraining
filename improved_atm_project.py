"""
Improve on your ATM mockup from last course to include the following:

1. Use functions
2. Include register, and login
3. Generate Account Number
4. Any other improvement you can think of (extra point)
"""

import random
import time
import datetime

date = datetime.datetime.now()

database = {}
account_balance = 0


def init():
    print("\n========== Welcome to zuriATM ==========")
    print("\nDo you have an account?")
    option = str.capitalize(input("Select Y - yes or N - no: "))

    if (option == "Y"):
        login()
    elif (option == "N"):
        print(register())
    else:
        print("Oops. You selected an invalid option")
        print("Do you wish to continue?")

        continue_option = str.capitalize(input("Select Y - yes or N - no: "))
        if (continue_option == "Y"):
            init()
        elif (continue_option == "N"):
            print("Thank you for banking with us.")
        else:
            print("Oof, wrong command.")

            confirm = str.capitalize(input("Try again? Y - yes and N - no: "))

            if (confirm == "Y"):
                init()
            elif (confirm == "N"):
                print("Thank you for banking with us.")


def register():
    print("\n ========== Register ========== ")

    email = input("\nYour Email Address: ")
    first_name = input("Your First Name: ")
    last_name = input("Your Last Name: ")
    password = int(input("Your Password: "))

    """
    account_number gets generated randomly
    """
    account_number = generate_acc_number()
    database[account_number] = [first_name, last_name, email, password]

    print("Your account has been created!")
    print(f"Your account number is: {account_number}")

    option = str.capitalize(
        input("\nDo you want to login now? Y - yes and N - no: ")
    )
    if (option == "Y"):
        login()
    elif (option == "N"):
        print("Thank you for banking with us.")
    else:
        print("Oof. You have selected an invalid option.")

    return database


def login():
    print("\n========== Login ========== ")
    _email = input("\nYour Email Address: ")
    _account_number = int(input("Your Account Number: "))
    _password = int(input("Your Password: "))

    if (_email and _password in database[_account_number]):
        print("\nAuthenticating. . .")

        time.sleep(5)
        print(f"Authenticated as {_email}!!\n")
        bankingOperation()
    else:
        print("Authentication failed!")
        confirm = str.capitalize(input("Try again? Y - yes and N - no: "))

        if (confirm == "Y"):
            login()
        elif (confirm == "N"):
            print("Thank you for banking with us.")


def generate_acc_number():
    print("\nGenerating Account Number...")
    time.sleep(2)
    print("Account Number Generated!")
    return random.randrange(000000000000, 11111111111)


def bankingOperation():
    print("\n========== Banking Operations ========== ")

    """
    The current date and time
    """
    time_date = date.strftime("%c")
    print(f"\nDate and Time: {time_date}")

    print("\nWhat banking operations do you want to do? \n1. Withdrawal \n2. Deposit \n3. Complaint")
    option = int(
        input("\nPlease select an operation: ")
    )
    if (option == 1):
        withdrawal()
    elif (option == 2):
        deposit()
    elif (option == 3):
        complaint()
    else:
        print("Oof. You have selected an invalid option.")


def withdrawal():
    print("\n========== Withdrawal Operation ========== ")

    print(account_balance)

    withdrawal = int(
        input("\nHow much would you like to withdrawal: ")
    )

    print("Withdrawaling cash. . .Please wait. . .\n")

    time.sleep(5)

    if (account_balance <= 0):
        print("Opps, you have cash in your account. Deposit, and try again.")
    elif (account_balance > withdrawal):
        account_balance -= withdrawal
        print("Take your cash. :-)")
    else:
        print("Wrong command!")

    print(f"You have #{account_balance} remaining in your account balance.")

    option = str.capitalize(
        input("\nWould you like to perform another transaction? Y - yes and N - no: "))
    if (option == "Y"):
        bankingOperation()
    elif (option == "N"):
        print("Thank you for banking with us today!")


def deposit():
    print("\n========== Deposit Operation ========== ")

    print(account_balance)

    deposit = int(
        input("\nHow much would you like to deposit: ")
    )
    account_balance += deposit
    print(f"Depositing cash. . .Please Wait! \n")

    time.sleep(5)
    print("Money deposited!")
    print(f"You now have #{account_balance} in your account.")

    option = str.capitalize(
        input("\nWould you like to perform another transaction? Y - yes and N - no: "))
    if (option == "Y"):
        bankingOperation()
    elif (option == "N"):
        print("Thank you for banking with us today!")


def complaint():
    print("\n========== Complain Operation ========== ")
    complainMsg = input("What issue will you like to report: ")
    print("\nPlease wait, while we send your complain.")

    """
    sends complain message to a txt file
    """
    time.sleep(5)
    f = open(f"complains/complain.txt", "w")
    f.write(complainMsg)
    f.close()

    print("Complain sent!\n")
    print("Thank you for contacting us.")

    option = str.capitalize(
        input("\nWould you like to perform another transaction? Y - yes and N - no: "))
    if (option == "Y"):
        bankingOperation()
    elif (option == "N"):
        print("Thank you for banking with us today!")


print(account_balance)
init()
