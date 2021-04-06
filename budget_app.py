class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        super().__init__()

    """
    Deposit funds to each category
    """
    def deposit_funds(self):
        print("Depositing funds... ")


    """
    Withdrawal funds from each category
    """
    def withdrawal_funds(self):
        print("Withdrawaling funds... ")


    """
    Computes each category balance
    """
    def computes_category_balance(self):
        print("Calculating balance for each category... ")


    """
    Transfers balance amount between categories
    """
    def transfer_balance(self):
        print("Transferring balance...")


budget = Budget("rice", "jeans", "games")

print(budget.transfer_balance())
