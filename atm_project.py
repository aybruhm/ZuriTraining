"""
This is an extended ATM project from the pervious classes,
taught. Features includes:

- user should see the current date and time (after they log in)
- when user selects option 1, present them with the following options:
    * input: how much would you like to withdrawal
    * output: take your cash
- when the user selects option 2, present them with the following options:
    * input: how much would you like to deposit?
    * output: current balance
- when the user selects complaint, present them with the following options:
    * input: what issue will you like to report?
    * output: "Thank you for contacting us"
"""

import datetime
date = datetime


authenticatedUsers = ['abram', 'dan', 'jacob']
authenticatedPwd = ['1234', '4567', '8900']


atm_machine = True
account_balance = 10000


while atm_machine:
    print("Hello, welcome to ATM mock project..\n Please Login In.")

    #Asks for user, username and password
    username = input("Your Username: ")
    password = input("Your Password: ")

    if (username in authenticatedUsers) and (password in authenticatedPwd):
        print("Authenticating..")
        print("You are now logged in!")
        print(f"The data and time is: ")

        option = input("Please select an option: \n 1 - withdrawal \n 2 - deposit \n 3 - complaint \n\n ")
        
        if (option == 1):
            withdrawal = input("How much would you like to withdrawal? ")
            account_balance -= withdrawal
            print("Withdrawaling cash. . .Please wait. . .\n Take your cash.")
        elif (option == 2):
            pass
        elif (option == 3):
            pass


    break