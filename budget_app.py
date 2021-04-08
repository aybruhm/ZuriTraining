"""
Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
1.  Depositing funds to each of the categories
2.  Withdrawing funds from each category
3.  Computing category balances
4.  Transferring balance amounts between categories
"""

class Budget:

    food_money = 0
    clothing_money = 0
    entertainment_money = 0

    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        super().__init__()

    """
    Deposit funds to each category
    """
    def deposit_funds(self):
        print("Depositing funds just got faster and better! \n")
        print("Categories: \n 1. Food \n 2. Clothing \n 3. Entertainment \n")
        choosed_category = int(input("Choose a category you intend to deposit in: "))
        
        if choosed_category == 1:
            print("You selected category 1: Food")
            amount_deposit = int(input("\nHow much do you want to deposit: "))
            Budget.food_money += amount_deposit
            print("Depositing to Food balance. . .Please Wait. . .Money deposited!")
            print(f"You now have {Budget.food_money} in your food balance. \n")

            """
            Gives the user an option to restart again.
            """
            restart_choice = str.capitalize(input("Do you want to try again? (Y) - yes or (N) - no: "))
            
            if restart_choice == "Y":
                start_option = int(
                    input("""\n What do you wish to do today? 
                        \n 1. Deposit funds \n 2. Withdrawal funds \n 3.Calculate your total balance \n 4. Transfer from a existing balance \n\n Please choose: """)
                    )
                if start_option == 1:
                    print("############################################")
                    budget.deposit_funds()
                elif start_option == 2:
                    print("############################################")
                    budget.withdrawal_funds()
                    print("############################################")
                elif start_option == 3:
                    budget.computes_category_balance()
                elif start_option == 4:
                    print("############################################")
                    budget.transfer_balance()
                else:
                    print("Thank you for banking with us!")

            elif restart_choice == "N":
                print("Thank you for checking in with us.")

            elif restart_choice == "N":
                print("Thank you for checking in with us.")


        elif choosed_category == 2:
            print("You selected category 2: Clothing")
            amount_deposit = int(input("\nHow much do you want to deposit: "))
            Budget.clothing_money += amount_deposit
            print("Depositing to Clothing balance. . .Please Wait. . .Money deposited!")
            print(f"You now have {Budget.clothing_money} in your food balance. \n")

            """
            Gives the user an option to restart again.
            """
            restart_choice = str.capitalize(input("Do you want to try again? (Y) - yes or (N) - no: "))
            
            if restart_choice == "Y":
                start_option = int(
                    input("""\n What do you wish to do today? 
                        \n 1. Deposit funds \n 2. Withdrawal funds \n 3.Calculate your total balance \n 4. Transfer from a existing balance \n\n Please choose: """)
                    )
                if start_option == 1:
                    print("############################################")
                    budget.deposit_funds()
                elif start_option == 2:
                    print("############################################")
                    budget.withdrawal_funds()
                    print("############################################")
                elif start_option == 3:
                    budget.computes_category_balance()
                elif start_option == 4:
                    print("############################################")
                    budget.transfer_balance()
                else:
                    print("Thank you for banking with us!")

            elif restart_choice == "N":
                print("Thank you for checking in with us.")

        elif choosed_category == 3:
            print("You selected category 3: Entertainment")
            amount_deposit = int(input("\nHow much do you want to deposit: "))
            Budget.entertainment_money += amount_deposit
            print("Depositing to Entertainment balance. . .Please Wait. . .Money deposited!")
            print(f"You now have {Budget.entertainment_money} in your food balance. \n")

            """
            Gives the user an option to restart again.
            """
            restart_choice = str.capitalize(input("Do you want to try again? (Y) - yes or (N) - no: "))
            
            if restart_choice == "Y":
                start_option = int(
                    input("""\n What do you wish to do today? 
                        \n 1. Deposit funds \n 2. Withdrawal funds \n 3.Calculate your total balance \n 4. Transfer from a existing balance \n\n Please choose: """)
                    )
                if start_option == 1:
                    print("############################################")
                    budget.deposit_funds()
                elif start_option == 2:
                    print("############################################")
                    budget.withdrawal_funds()
                    print("############################################")
                elif start_option == 3:
                    budget.computes_category_balance()
                elif start_option == 4:
                    print("############################################")
                    budget.transfer_balance()
                else:
                    print("Thank you for banking with us!")

            elif restart_choice == "N":
                print("Thank you for checking in with us.")

            elif restart_choice == "N":
                print("Thank you for checking in with us.")
        else:
            print("Oops. No such option in category list.")
            restart_choice = input("Do you want to try again? (Y) - yes or (N) - no: ")
            
            if restart_choice == "Y":
                budget.deposit_funds()
            elif restart_choice == "N":
                print("Thank you for checking in with us.")

    """
    Withdrawal funds from each category
    """
    def withdrawal_funds(self):
        print("Withdrawaling funds just got faster and better! \n")
        print("Categories: \n 1. Food \n 2. Clothing \n 3. Entertainment \n")
        choosed_category = int(input("Choose a category you intend to withdrawal from: "))

        if choosed_category == 1:
            print("")
        elif choosed_category == 2:
            print("")
        elif choosed_category == 3:
            print("")
        else:
            print("Oops. No such option in category list.")
            restart_choice = input("Do you want to try again? (Y) - yes or (N) - no: ")
            
            if restart_choice == "Y":
                budget.deposit_funds()
            elif restart_choice == "N":
                print("Thank you for checking in with us.")

    """
    Computes each category balance
    """
    def computes_category_balance(self):

        category_prices = {
            'food': 100,
            'clothing': 300,
            'entertainment': 700
        }
        print(category_prices["entertainment"])


    """
    Transfers balance amount between categories
    """
    def transfer_balance(self):
        print("Transferring balance...")


budget = Budget("rice", "jeans", "games")

print(budget.deposit_funds())
