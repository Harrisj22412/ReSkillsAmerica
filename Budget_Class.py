class Category:
    
    #constructor
    def __init__(self, category, amount): 
        self.category = category
        self.amount = amount
    
    #methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def check_balance(self, amount):
        print(amount)

    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)
        


    def transfer(self, amount):
        self.amount += amount
        return 'You have successfully transfered {} into your account your new amount is {}'.format(amount, self.amount)

        


food_category = Category("Food", 500)
clothing_category = Category("Clothing", 300)
car_category = Category("Car Expenses", 600)

print(food_category.deposit(250))
print(food_category.budget_balance())
print(clothing_category.transfer(300))



