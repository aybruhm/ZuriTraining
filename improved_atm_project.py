"""
Improve on your ATM mockup from last course to include the following:

1. Use functions
2. Include register, and login
3. Generate Account Number
4. Any other improvement you can think of (extra point)
"""

import random
import time

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
    pass


def withdrawal():
    pass


def deposit():
    pass


def complaint():
    pass


init()
