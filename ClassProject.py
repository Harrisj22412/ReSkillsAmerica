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
        return 'This is the current balance: {}'.format(self.amount)

    def check_balance(self, amount):
        if amount > self.amount:
            print(amount)
            return True
        else:
            return False

    def withdraw(self, amount):
        self.amount -= amount 
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def transfer(self, amount, category):
        if self.amount < amount:
            self.amount += amount
            print('You will need to transfer funds.')
        else:
            print('No transaction was needed, have a great rest of the day.')


    food_category = Category('Food', 500)
    clothing_category = Category('Clothing', 600)
    car_category = Category('Car Expenses', 400)


    print(food_category.deposit(250))
    print(food_category.budget_balance())