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

    # Asks for user's username
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
            print("""============. . .Authentication Successful. . .============\n""")

            # Capitalize the first letter "a" -> "A"
            print(f"Welcome, {str.capitalize(username)}")

            """
            TODO:
            - import date module
            - show time and date
            """
        else:
            print(
                """============ You are not in our database, please try again. ============""")
            break

        print("""
        These are the allowed options:\n
        1. Withdrawal\n
        2. Cash Deposit\n
        3. Complaint
        """)

        allowedOption = int(input("Please select an option: "))

        if (allowedOption == 1):
            withdrawal = int(
                input("How much would you like to withdrawal? \n")
            )
            print("Withdrawaling cash. . .Please wait. . .")
            account_balance -= withdrawal
            print("Take your cash. :-)")
            print(f"You have #{account_balance} remaining in your account.")

        elif (allowedOption == 2):
            print(
                f"You now have #{account_balance} in your account.\n"
            )
            deposit = int(
                input("How much would you like to deposit? ")
            )
            account_balance += deposit
            print(
                f"Depositing cash. . .Cash deposited! \n")
            print(f"You now have #{account_balance} in your account.")

        elif (allowedOption == 3):
            complainMsg = input("What is your complain? \n\n")
            print("\n\nPlease wait, while we send your complain.")

            # sends complain message to a txt file
            with (open("complain.txt")) as f:
                f.write(complainMsg)
                f.close()

            print("Complain sent!\n")
            print("Thank you for contacting us.")
        else:
            print("Ooof. You have select an incorrect option. Please try again.")

    break
