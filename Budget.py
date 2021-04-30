class Budget:
    
    #constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    #methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited ${} into your {} budget.".format(amount, self.category)


    def check_balance(self):
        return "Your current {} balance is ${}.".format(self.category, self.amount)


    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount
            return "You have succesfully withdrawn ${} out of your {} budget.".format(amount, self.category)

        else:
            return "Withdrawal amount exceeds account balance. Please try again."


    def transfer(self, amount, category):
        if self.check_balance():
            self.amount <= amount
            self.amount -= amount
            category.amount += amount
            return "You have successfully transferred ${} from your {} budget into your {} budget.".format(amount, self.category, category.category)

        else:
            return "Amount to transfer exceeds account balance. Please try again."


food_budget = Budget("FOOD", 325)
clothing_budget = Budget("CLOTHING", 100)
entertainment_budget = Budget("ENTERTAINMENT", 150)
emergency_budget = Budget("EMERGENCY", 500)


print(food_budget.deposit(56))
print(clothing_budget.check_balance())
print(emergency_budget.withdraw(35))
print(emergency_budget.transfer(75, food_budget))
