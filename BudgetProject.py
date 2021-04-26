#Please run each function one at a time.


global balance
import random 
global amount


class Budget:
    #amount = []

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        self.balance = 300
        

    def transfer(self):
        print('Transfer was successfully made for your payment today.')
        confirmation_number = random.randrange(1111, 9999)
        print(confirmation_number)


    def deposit(self, amount, balance):
        
        balance += amount
        deposit_response = input('You just got paid, would you like to check your balance?: \n')
        if deposit_response  == 'yes':
            print(balance)
        elif deposit_response == 'no':
            print("Thanks for choosing Chase Bank, have a great day.")
         
        else: print('Invalid choice selection please try again.')

    def withdrawal(self, balance, amount):
        amount = int(amount)
        request = input('How much would you like to withdraw today?: \n')
        balance -= amount
        request = balance
        request = int()
        if request <= balance :
            request -= balance
            check = input("Would you now like to check your balance?: \n")
            if check == 'yes':
                print(balance)
                print("Thanks for choosing Chase Bank, have a great day!")
            elif check == 'no':
                print("Thanks for choosing Chase Bank, have a great day!")

        elif request > balance:
            print('Sorry, this account has insufficient funds.')
            transfer_opt = input('Would you like to  transfer funds to this account? \n')
            if transfer_opt == 'yes':
                print(balance)
                
            elif transfer_opt == 'no':
                print("Thanks for choosing Chase Bank, have a great day!")

        else: print('Invalid selection option please try again.')
        #withdrawal(amount)

    def check_balance(self, balance):
        print(balance)
    
class Food(Budget):
    def __init__(self, item, amount):
        super().__init__(self, amount)
        self.item = item
        self.amount = amount
        
        

class Clothing(Budget):
    def __init__(self, item, amount):
        super().__init__(self, amount)
        self.item = item
        self.amount = str(amount)

    def clothing_expenses(self):
        
        print('These are the expenses for' + ' ' + self.item + ' '+ self.amount)
        

class Car(Budget):
    def __init__(self, model, year, amount):
        super().__init__(self, amount)
        
        self.model = model
        self.year = year
        self.amount = amount

    def car_details(self, amount):
        return '{} {} {}'.format(self.model, self.year, self.amount)
        print(self.model, self.year, self.amount)
        

#run each function one at a time, to view the operations


my_car = Car('Telsa', 2021 , 550)
#print(my_car.car_details(550))

jalen_budget = Budget('Entertainment ', 600)

#print(jalen_budget.expenses(300))


#jalen_budget.withdrawal(600)

#jalen_budget.deposit(500, 300)


clothing_category = Clothing('Nike', '300')
#print(clothing_category.clothing_expenses())





#print(Budget(category_1))

#print(help(Budget))

