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


def init():
    print("\nWelcome to IsraelBANK")
    print("Do you have an account?")
    option = str.capitalize(input("Select Y - yes or N - no: "))

    if (option == "Y"):
        login()
    elif (option == "N"):
        print(register())
    else:
        print("Oops. You selected an invalid option")
        print("Do you wish to continue?")
        continue_option = str.capitalize(input("Select Y - yes or N - no: "))


def register():
    print("\n############ Register ############")

    email = input("Your Email Address: ")
    first_name = input("Your First Name: ")
    last_name = input("Your Last Name: ")
    password = int(input("Your Password: "))
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
    print("\n############ Login ############")
    email = input("Your Email Address: ")
    password = int(input("Your Password: "))

    for email, password in database.items():
        print(email, password)


def generate_acc_number():
    print("\nGenerating Account Number...")
    time.sleep(2)
    print("Account Number Generated!")
    return random.randrange(000000000000, 11111111111)


def bankingOperation():
    print("\n############ Banking Operations ############")

    """
    The current date and time
    """
    time_date = date.strftime("%c")
    print(f"\nDate and Time: {time_date}")

    print("What banking operations do you want to do? \n1. Withdrawal \n2. Deposit \n3. Complaint")
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
    print("############ Withdrawal Operation ############")


def deposit():
    print("############ Deposit Operation ############")


def complaint():
    print("\n############ Complain Operation ############")
    complainMsg = input("What issue will you like to report? \n\n")
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


bankingOperation()
