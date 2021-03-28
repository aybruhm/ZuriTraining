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
    print("""
    ===========================================
    Welcome to ATM mock project.. Please Login In.
    ===========================================\n \n""")

    # Asks for user, username and password
    username = input("Your Username: ")

    """
    For a username not found in the authenticatedUsers, line 42 throws a value error;
    causing the whole program to break. I solved this by using the try/except block.
    """
    try:
        userID = authenticatedUsers.index(username)
    except ValueError:
        print("Oops, we can not find you in our users list. :-) \n")
        break

    if (username in authenticatedUsers):
        print("""============. . .Authenticating. . .============\n""")

        password = input(f"Password for {username}: ")
        if (password in authenticatedPwd[userID]):
            print("""============. . .Authentication Successful. . .============""")
            print(f"Welcome, {username}")
    else:
        print(
            """============ You are not in our database, please try again. ============""")

        option = input(
            "Please select an option: \n 1 - withdrawal \n 2 - deposit \n 3 - complaint \n\n ")

        if (option == 1):
            withdrawal = input("How much would you like to withdrawal? ")
            account_balance -= withdrawal
            print("Withdrawaling cash. . .Please wait. . .\n Take your cash.")

        elif (option == 2):
            deposit = input("How much would you like to deposit? ")
            account_balance += deposit
            print(
                f"Cash deposited. You now have {account_balance} in your account.")

        elif (option == 3):
            pass

    break
