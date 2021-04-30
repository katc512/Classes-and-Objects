class Budget:
    
    #constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    #methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited ${} into your {} budget.".format(amount, self.category)


    def check_balance(self, amount):
        balance = self.amount
        return "Your current balance is ${}".format(amount, self.category)


    def withdraw(self, amount):
        self.amount -= amount
        return "You have succesfully withdrawn ${} out of your {} budget.".format(amount, self.category)


    def transfer(self, amount):
        pass


food_budget = Budget("FOOD", 325)
clothing_budget = Budget("CLOTHING", 100)
entertainment_budget = Budget("ENTERTAINMENT", 150)
emergency_budget = Budget("EMERGENCY", 500)

print(food_budget.deposit(56))
print(emergency_budget.withdraw(35))
