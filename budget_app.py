"""
Create a Budget class that can instantiate objects based on 
different budget categories like food, clothing, and entertainment. 
These objects should allow for: 

1.  Depositing funds to each of the categories
2.  Withdrawing funds from each category
3.  Computing category balances
4.  Transferring balance amounts between categories
"""

import time


class Budget:

    food_money = 0
    clothing_money = 0
    entertainment_money = 0

    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        super().__init__()

    def startBudgetApp(self):
        """
        Starts the budget app and gives the user an option to choose what he/she wants to do.
        """
        print("\n========== Welcome to our budget app. ==========")
        choice = int(
            input("""What do you wish to do? \n\n 1. Deposit money \n 2. Withdrawal money \n 3. Calculate total balance \n 4. Transfer money \n\nPlease choose: """)
        )

        if choice == 1:
            budget.deposit_funds()
        elif choice == 2:
            budget.withdrawal_funds()
        elif choice == 3:
            budget.computes_balance()
        elif choice == 4:
            budget.transfer_balance()
        else:
            print("Opps. Seems like you have selected an invalid option.")
            budget.restartBudgetApp()

    def restartBudgetApp(self):
        """
        Gives the user an option to restart again.
        """
        restart_choice = str.capitalize(
            input("Do you want to try again? (Y) - yes or (N) - no: "))

        if restart_choice == "Y":
            budget.startBudgetApp(self)
        elif restart_choice == "N":
            print("Thank you for checking in with us.")

    """
    Deposit funds to each category
    """

    def deposit_funds(self):
        print("Depositing funds just got faster and better! \n")
        print("Categories: \n 1. Food \n 2. Clothing \n 3. Entertainment \n")
        choosed_category = int(
            input("Choose a category you intend to deposit in: "))

        if choosed_category == 1:
            print("You selected category 1: Food")
            amount_deposit = int(input("\nHow much do you want to deposit: "))
            Budget.food_money += amount_deposit
            print("Depositing to Food balance. . .Please Wait. . .Money deposited!")
            print(f"You now have {Budget.food_money} in your food balance. \n")

            """
            Gives the user an option to restart again.
            """
            restart_choice = str.capitalize(
                input("Do you want to try again? (Y) - yes or (N) - no: "))

            if restart_choice == "Y":
                Budget.startBudgetApp(self)
            elif restart_choice == "N":
                print("Thank you for checking in with us.")

        elif choosed_category == 2:
            print("You selected category 2: Clothing")
            amount_deposit = int(input("\nHow much do you want to deposit: "))
            Budget.clothing_money += amount_deposit
            print("Depositing to Clothing balance. . .Please Wait. . .Money deposited!")
            print(
                f"You now have {Budget.clothing_money} in your food balance. \n")

            """
            Gives the user an option to restart again.
            """
            restart_choice = str.capitalize(
                input("Do you want to try again? (Y) - yes or (N) - no: "))

            if restart_choice == "Y":
                Budget.startBudgetApp(self)
            elif restart_choice == "N":
                print("Thank you for checking in with us.")

        elif choosed_category == 3:
            print("You selected category 3: Entertainment")
            amount_deposit = int(input("\nHow much do you want to deposit: "))
            Budget.entertainment_money += amount_deposit
            print(
                "Depositing to Entertainment balance. . .Please Wait. . .Money deposited!")
            print(
                f"You now have {Budget.entertainment_money} in your food balance. \n")

            """
            Gives the user an option to restart again.
            """
            restart_choice = str.capitalize(
                input("Do you want to try again? (Y) - yes or (N) - no: "))

            if restart_choice == "Y":
                Budget.startBudgetApp(self)
            elif restart_choice == "N":
                print("Thank you for checking in with us.")

        else:
            print("Oops. No such option in category list.")
            restart_choice = input(
                "Do you want to try again? (Y) - yes or (N) - no: ")

            if restart_choice == "Y":
                budget.restartBudgetApp()
            elif restart_choice == "N":
                print("Thank you for checking in with us.")

    """
    Withdrawal funds from each category
    """

    def withdrawal_funds(self):
        print("Withdrawaling funds just got faster and better! \n")
        print("Categories: \n 1. Food \n 2. Clothing \n 3. Entertainment \n")
        choosed_category = int(
            input("Choose a category you intend to withdrawal from: "))

        if choosed_category == 1:
            print("You selected category 1: Food")
            amount_withdrawal = int(
                input("\nHow much do you want to withdrawal: "))
            total_balance = Budget.food_money
            print(f"You have {total_balance} in your balance")

            if (total_balance <= 0):
                print(
                    f"\nYou have {total_balance} in your balance. Do you wish to continue?\n")
                choice = str.capitalize(
                    input("Choose a choice (Y) - yes or (N) - no: "))
                if choice == "Y":
                    print("\n##########################")
                    budget.startBudgetApp()
                elif choice == "N":
                    print("Thank you for checking in with us.")

            elif (total_balance > amount_withdrawal):
                total_balance -= amount_withdrawal
                print(
                    "Withdrawaling from Food balance. . .Please Wait. . .Money withdrawaled!")
                print(f"You now have {total_balance} in your food balance. \n")

            elif (total_balance < amount_withdrawal):
                print("You don't have up to the requested amount.")

            """
            Calls restartBudgetApp, giving the user an option to restart again.
            """
            budget.restartBudgetApp()

        elif choosed_category == 2:
            print("You selected category 2: Clothing")
            amount_withdrawal = int(
                input("\nHow much do you want to withdrawal: "))
            total_balance = Budget.clothing_money
            print(f"You have {total_balance} in your balance")

            if (total_balance <= 0):
                print(
                    f"\nYou have {total_balance} in your balance. Do you wish to continue?")
                choice = str.capitalize(
                    input("Choose a choice (Y) - yes or (N) - no: "))
                if choice == "Y":
                    print("\n##########################")
                    budget.startBudgetApp()
                elif choice == "N":
                    print("Thank you for checking in with us.")

            elif (total_balance > amount_withdrawal):
                total_balance -= amount_withdrawal
                print(
                    "Withdrawaling from Clothing balance. . .Please Wait. . .Money withdrawaled!")
                print(f"You now have {total_balance} in your food balance. \n")

            elif (total_balance < amount_withdrawal):
                print("You don't have up to the requested amount.")

            """
            Calls restartBudgetApp, giving the user an option to restart again.
            """
            budget.restartBudgetApp()

        elif choosed_category == 3:
            print("You selected category 3: Entertainment")
            amount_withdrawal = int(
                input("\nHow much do you want to withdrawal: "))
            total_balance = Budget.entertainment_money
            print(f"You have {total_balance} in your balance")

            if total_balance <= 0:
                print(
                    f"\nYou have {total_balance} in your balance. Do you wish to continue?")
                choice = str.capitalize(
                    input("Choose a choice (Y) - yes or (N) - no: "))
                if choice == "Y":
                    print("\n##########################")
                    budget.startBudgetApp()
                elif choice == "N":
                    print("Thank you for checking in with us.")

            elif (total_balance > amount_withdrawal):
                total_balance -= amount_withdrawal
                print(
                    "Withdrawaling from Entertainment balance. . .Please Wait. . .Money withdrawaled!")
                print(f"You now have {total_balance} in your food balance. \n")

            elif (total_balance < amount_withdrawal):
                print("You don't have up to the requested amount.")

            """
            Calls restartBudgetApp, giving the user an option to restart again.
            """
            budget.restartBudgetApp()

        else:
            print("Oops. No such option in category list.")
            restart_choice = input(
                "Do you want to try again? (Y) - yes or (N) - no: ")

            if restart_choice == "Y":
                budget.deposit_funds()
            elif restart_choice == "N":
                print("Thank you for checking in with us.")

    """
    Computes each category balance
    """

    def computes_balance(self):
        print("Knowing your balance just got faster and better! \n")
        print("Categories: \n 1. Food \n 2. Clothing \n 3. Entertainment \n 4. All \n")
        choosed_category = int(
            input("Choose a category you intend to withdrawal from: "))

        if choosed_category == 1:
            print("\nYou choose Category 1, which is Food.")
            print("Please wait, while we calculate category 1 balance. . .")

            time.sleep(5)
            print(f"\nFood balance: #{budget.food_money} \n")

            """
            Calls restartBudgetApp, giving the user an option to restart again.
            """
            budget.restartBudgetApp()

        elif choosed_category == 2:
            print("\nYou choose Category 2, which is Clothing.")
            print("Please wait, while we calculate category 2 balance. . .")

            time.sleep(5)
            print(f"\nClothing balance: #{budget.clothing_money} \n")

            """
            Calls restartBudgetApp, giving the user an option to restart again.
            """
            budget.restartBudgetApp()

        elif choosed_category == 3:
            print("\nYou choose Category 3, which is Entertainment.")
            print("Please wait, while we calculate category 3 balance. . .")

            time.sleep(5)
            print(f"\nEntertainment balance: #{budget.entertainment_money} \n")

            """
            Calls restartBudgetApp, giving the user an option to restart again.
            """
            budget.restartBudgetApp()

        elif choosed_category == 4:
            print(
                "\nYou found our newest feature, you can now know the balance of all your category.")
            print("Please wait...")

            print("We are calculating your categories balances. . .")
            time.sleep(5)
            print(
                f"\nResults: \nFood balance - #{budget.food_money} \nClothing balance - #{budget.clothing_money} \nEntertainment balance - #{budget.entertainment_money} \n")

            """
            Calls restartBudgetApp, giving the user an option to restart again.
            """
            budget.restartBudgetApp()

        else:
            print("Oops. No such option in category list.")
            restart_choice = input(
                "Do you want to try again? (Y) - yes or (N) - no: ")

            if restart_choice == "Y":
                budget.deposit_funds()
            elif restart_choice == "N":
                print("Thank you for checking in with us.")

    """
    Transfers balance amount between categories
    """

    def transfer_balance(self):
        food_balance = budget.food_money
        clothing_balance = budget.clothing_money
        entertainment_balance = budget.entertainment_money

        print("Transferring funds just got faster and better! \n")
        print("Categories: \n 1. Food \n 2. Clothing \n 3. Entertainment \n")

        transfer_from = int(
            input("Choose a category you intend to transfer from: "))
        from_amount = int(input("Enter amount: "))
        transfer_to = int(
            input("Choose a category you intend to transfer to: "))

        if transfer_from == 1:
            if transfer_to == 1:
                print(
                    "\nWe apologize, but you can not transfer from and to the same category.")

                """
                Calls restartBudgetApp, giving the user an option to restart again.
                """
                budget.restartBudgetApp()

            elif transfer_to == 2:
                print("\nTransferring funds from Food to Clothing. . .")

                """
                Conditional statement, to check if the category has enough funds or not.
                """
                if (food_balance == 0):
                    print(
                        f"\nYou have #{food_balance} in your balance. Do you wish to continue?\n")

                    choice = str.capitalize(
                        input("Choose a choice (Y) - yes or (N) - no: "))
                    if choice == "Y":
                        print("\n##########################")
                        budget.startBudgetApp()
                    elif choice == "N":
                        print("Thank you for checking in with us.")

                elif (food_balance > from_amount):
                    food_balance -= from_amount
                    print(f"You now have {food_balance} in your wallet.\n")

                elif (food_balance < from_amount):
                    print("You don't have up to the requested amount.")

                """
                Waits for 5 seconds, while transferring funds from the selected category.
                """
                time.sleep(5)
                clothing_balance += from_amount
                print("\nMoney transferred!")
                print(
                    f"You now have {clothing_balance} in your clothing wallet.")

                """
                Calls restartBudgetApp, giving the user an option to restart again.
                """
                budget.restartBudgetApp()

            elif transfer_to == 3:
                print("Transferring funds from Food to Entertainment. . .")

                """
                Conditional statement, to check if the category has enough funds or not.
                """
                if (food_balance == 0):
                    print(
                        f"\nYou have #{food_balance} in your balance. Do you wish to continue?\n")

                    choice = str.capitalize(
                        input("Choose a choice (Y) - yes or (N) - no: "))
                    if choice == "Y":
                        print("\n##########################")
                        budget.startBudgetApp()
                    elif choice == "N":
                        print("Thank you for checking in with us.")

                elif (food_balance > from_amount):
                    food_balance -= from_amount
                    print(f"You now have {food_balance} in your wallet.\n")

                elif (food_balance < from_amount):
                    print("You don't have up to the requested amount.")

                """
                Waits for 5 seconds, while transferring funds from the selected category.
                """
                time.sleep(5)
                entertainment_balance += from_amount
                print("Money transferred!")
                print(
                    f"You now have {entertainment_balance} in your entertainment wallet.\n")

                """
                Calls restartBudgetApp, giving the user an option to restart again.
                """
                budget.restartBudgetApp()

            else:
                print("You have selected an invalid option.")

        elif transfer_from == 2:
            if transfer_to == 1:
                print("\nTransferring funds from Clothing to Food. . .")

                if (clothing_balance == 0):
                    print(
                        f"\nYou have #{clothing_balance} in your balance. Do you wish to continue?\n")

                    choice = str.capitalize(
                        input("Choose a choice (Y) - yes or (N) - no: "))
                    if choice == "Y":
                        print("\n##########################")
                        budget.startBudgetApp()
                    elif choice == "N":
                        print("Thank you for checking in with us.")

                elif (clothing_balance > from_amount):
                    clothing_balance -= from_amount
                    print(f"You now have {clothing_balance} in your wallet.")

                elif (clothing_balance < from_amount):
                    print("You don't have up to the requested amount.")

                """
                Waits for 5 seconds, while transferring funds from the selected category.
                """
                time.sleep(5)
                food_money += from_amount
                print("\nMoney transferred!")
                print(f"You now have {food_money} in your wallet.")

                """
                Calls restartBudgetApp, giving the user an option to restart again.
                """
                budget.restartBudgetApp()

            elif transfer_to == 2:
                print(
                    "\nWe apologize, but you can not transfer from and to the same category.")

                """
                Calls restartBudgetApp, giving the user an option to restart again.
                """
                budget.restartBudgetApp()

            elif transfer_to == 3:
                print("\nTransferring funds from Clothing to Entertainment. . .")

                """
                Conditional statement, to check if the category has enough funds or not.
                """
                if (clothing_balance == 0):
                    print(
                        f"\nYou have #{clothing_balance} in your balance. Do you wish to continue?\n")

                    choice = str.capitalize(
                        input("Choose a choice (Y) - yes or (N) - no: "))
                    if choice == "Y":
                        print("\n##########################")
                        budget.startBudgetApp()
                    elif choice == "N":
                        print("Thank you for checking in with us.")

                elif (clothing_balance > from_amount):
                    clothing_balance -= from_amount
                    print(f"You now have {food_balance} in your wallet.\n")

                elif (clothing_balance < from_amount):
                    print("You don't have up to the requested amount.")

                """
                Waits for 5 seconds, while transferring funds from the selected category.
                """
                time.sleep(5)
                entertainment_money += from_amount
                print("\nMoney transferred!")
                print(f"You now have {entertainment_money} in your wallet.")

                """
                Calls restartBudgetApp, giving the user an option to restart again.
                """
                budget.restartBudgetApp()

        elif transfer_from == 3:
            if transfer_to == 1:
                print("\nTransferring funds from Entertainment to Food. . .")

                """
                Conditional statement, to check if the category has enough funds or not.
                """
                if (entertainment_balance == 0):
                    print(
                        f"\nYou have #{clothing_balance} in your balance. Do you wish to continue?\n")

                    choice = str.capitalize(
                        input("Choose a choice (Y) - yes or (N) - no: "))
                    if choice == "Y":
                        print("\n##########################")
                        budget.startBudgetApp()
                    elif choice == "N":
                        print("Thank you for checking in with us.")

                elif (entertainment_balance > from_amount):
                    entertainment_balance -= from_amount
                    print(
                        f"You now have {entertainment_balance} in your wallet.")

                elif (entertainment_balance < from_amount):
                    print("You don't have up to the requested amount.")

                """
                Waits for 5 seconds, while transferring funds from the selected category.
                """
                time.sleep(5)
                food_balance += from_amount
                print("\nMoney transferred!")
                print(f"You now have {food_balance} in your wallet.")

                """
                Calls restartBudgetApp, giving the user an option to restart again.
                """
                budget.restartBudgetApp()

            elif transfer_to == 2:
                print("\nTransferring funds from Entertainment to Clothing. . .")

                """
                Conditional statement, to check if the category has enough funds or not.
                """
                if (entertainment_balance == 0):
                    print(
                        f"\nYou have #{clothing_balance} in your balance. Do you wish to continue?\n")

                    choice = str.capitalize(
                        input("Choose a choice (Y) - yes or (N) - no: "))
                    if choice == "Y":
                        print("\n##########################")
                        budget.startBudgetApp()
                    elif choice == "N":
                        print("Thank you for checking in with us.")

                elif (entertainment_balance > from_amount):
                    entertainment_balance -= from_amount
                    print(
                        f"You now have {entertainment_balance} in your wallet.")

                elif (entertainment_balance < from_amount):
                    print("You don't have up to the requested amount.")

                """
                Waits for 5 seconds, while transferring funds from the selected category.
                """
                time.sleep(5)
                clothing_balance += from_amount
                print("\nMoney transferred!")
                print(f"You now have {clothing_balance} in your wallet.")

                """
                Calls restartBudgetApp, giving the user an option to restart again.
                """
                budget.restartBudgetApp()

            elif transfer_to == 3:
                print(
                    "\nWe apologize, but you can not transfer from and to the same category.")

                """
                Calls restartBudgetApp, giving the user an option to restart again.
                """
                budget.restartBudgetApp()

        else:
            print("You have selected an invalid option.")

            """
            Calls restartBudgetApp, giving the user an option to restart again.
            """
            budget.restartBudgetApp()


budget = Budget("food", "clothing", "entertainment")
budget.startBudgetApp()
