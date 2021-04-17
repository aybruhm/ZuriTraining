"""
Author: Israel Abraham
Update: April 16 2021, 14:40

Improve on your ATM mockup from last course to include the following:

1. Use functions
2. Include register, and login
3. Generate Account Number
4. Any other improvement you can think of (extra point)
"""

"""
New Improvements I implemented: 

5. Check balance
6. Rate our service

"""

import random
import time
import datetime

date = datetime.datetime.now()

database = {}
dash = "=" * 10


def init():
    print(f"\n{dash} Welcome to zuriATM {dash}")
    print("\nDo you have an account?")
    option = str.capitalize(input("Select Y - yes or N - no: "))

    if (option == "Y"):
        try:
            login()
        except KeyError:
            print("\nxxxxxxxxxx Oga, please register an account first. xxxxxxxxxx")
            init()

    elif (option == "N"):
        register()

    else:
        print("Oops. You selected an invalid option")
        print("Do you wish to continue?")

        continue_option = str.capitalize(input("Select Y - yes or N - no: "))
        if (continue_option == "Y"):
            init()
        elif (continue_option == "N"):
            print("Thank you for banking with us.")
            exit()
        else:
            print("Oof, wrong command.")

            confirm = str.capitalize(input("Try again? Y - yes and N - no: "))

            if (confirm == "Y"):
                init()
            elif (confirm == "N"):
                print("Thank you for banking with us.")
                exit()


def register():
    print(f"\n {dash} Register {dash} ")

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
    print(f"\n{dash} Login {dash} ")
    _email = input("\nYour Email Address: ")
    _account_number = int(input("Your Account Number: "))
    _password = int(input("Your Password: "))
    account_balance = 0

    if (_email and _password in database[_account_number]):
        print("\nAuthenticating. . .")

        user = database[_account_number][0]

        time.sleep(5)
        print(f"Authenticated as {user}!!")
        print(f"{user} you have #{account_balance} in your account.\n")
        bankingOperation(user, account_balance)
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


def bankingOperation(user, account_balance):
    print(f"\n{dash} Banking Operations {dash} ")

    """
    The current date and time
    """
    time_date = date.strftime("%c")
    print(f"\nDate and Time: {time_date}")

    print("\nWhat banking operations do you want to do? \n\n[1] - Withdrawal \n[2] - Deposit \n[3] - Complaint \n[4] - Check Balance \n[5] - Rate Us \n[6] - Exit")
    option = int(
        input("\nPlease choose an operation: ")
    )
    if (option == 1):
        withdrawal(user, account_balance)

    elif (option == 2):
        deposit(user, account_balance)

    elif (option == 3):
        complaint(user)

    elif (option == 4):
        checkBalance(user, account_balance)
        
    elif (option == 5):
        rateUs(user)

    elif (option == 6):
        print("Thank you for using our service. :-)")
        exit()
    else:
        print("Oof. You have selected an invalid option.")


def withdrawal(user, account_balance):
    print(f"\n{dash} Withdrawal Operation {dash} ")
    print(f"{user}, you have #{account_balance} in your account.")

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
        print(f"{user}, you now have #{account_balance} in your account.")
    else:
        print("Wrong command!")

    print(f"You have #{account_balance} remaining in your account balance.")

    option = str.capitalize(
        input("\nWould you like to perform another transaction? [Y] - yes or [N] - no: "))
    if (option == "Y"):
        bankingOperation(user, account_balance)
    elif (option == "N"):
        print("Thank you for banking with us today!")


def deposit(user, account_balance):
    print(f"\n{dash} Deposit Operation {dash} ")
    print(f"{user}, you have #{account_balance} in your account.")

    deposit = int(
        input("\nHow much would you like to deposit: ")
    )
    account_balance += deposit
    print(f"Depositing cash. . .Please Wait! \n")

    time.sleep(5)
    print("Money deposited!")
    print(f"{user}, you now have #{account_balance} in your account.")

    option = str.capitalize(
        input("\nWould you like to perform another transaction? [Y] - yes or [N] - no: "))
    if (option == "Y"):
        bankingOperation(user, account_balance)
    elif (option == "N"):
        print("Thank you for banking with us today!")


def complaint(user):
    print(f"\n{dash} Complain Operation {dash} ")
    complainMsg = input("\nWhat issue will you like to report: ")
    print("\nPlease wait, while we send your complain.")

    """
    sends complain message to a txt file
    """
    time.sleep(5)
    f = open(f"complains/{user}-complain.txt", "w")
    f.write(complainMsg)
    f.close()

    print("Complain sent!\n")
    print("Thank you for contacting us.")

    option = str.capitalize(
        input("\nWould you like to perform another transaction? Y - yes and N - no: "))
    if (option == "Y"):
        bankingOperation(user, account_balance)
    elif (option == "N"):
        print("Thank you for banking with us today!")


def checkBalance(user, account_balance):
    print(f"\n{dash} Check Your Balance {dash}")
    
    print(f"\nGive us a minute as we validate your account...")

    time.sleep(5)
    print(f"\n{user}, your account has been validated.\nYou have {account_balance} in your account.")

    option = str.capitalize(input("\nDo you wish to continue? [Y] - yes or [N] - no: "))
    if (option == "Y"):
        bankingOperation(user, account_balance)
    elif (option == "N"):
        choice = str.capitalize(
            ("Wait.. quickly tell us what you think about our service? [Y] - sure or [N] - who cares: ")
        )
        if (choice == "Y"):
            rateUs(user, account_balance)
        elif (choice == "N"):
            print("Thank you for your time.")
            exit()
    else:
        print("Oof, wrong command.")
        exit()




def rateUs(user):
    print(f"\n{dash} Rate Us {dash}")
    option = int(
        input("\nHow many stars would you rate our system?\n\n[5] - Excellent\n[4] - Very Good\n[3] - Good\n[2] - Manageable\n[1] - Poor\n[0] - Very Poor\n\nPlease choose an option: ")
    )

    if (option == 5):
        print(f"Oh my.. You rated our system the best of best. Thank you, {user}.\n")
    elif (option == 4):
        print(f"Thank you, {user}. We are working very hard to make you smile.\n")
    elif (option == 3):
        print(f"Thank you, {user}. We are constantly improving our system.\n")
    elif (option == 2):
        print(f"Oof, our system has been slow and tiredly annoying, {user}. We appreciate your feedback.\n")
    elif (option == 1):
        print(f";-; our system is annoyingly not responsding fast, {user}. We apologize for the inconviences you faced.\n")
    else:
        print("Oof. Wrong command.")
        exit()


init()
