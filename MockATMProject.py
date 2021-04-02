#\n = drops to the next line

name = input('What is your name? \n')
allowedUsers = ['Jalen', 'Mike', 'Tony', 'Lisa']
allowedPassword = ['PasswordJalen', 'PasswordMike', 'PasswordTony', 'PasswordLisa']
from datetime import date
today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print( d1)

from datetime import datetime
now = datetime.now()
print(now)



if(name in allowedUsers):
    password = input('What is  your password? \n')
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome  %s' %  name)
        print('These are the available options:' ) 
        print('1. Withdrawl')
        print('2. Deposit')
        print('3. Complaint')

        selectOption = int(input('Please select an option:' ))
        print(d1, now)
        userInput = True 
        print(selectOption)
        if(selectOption == 1):
            print('You selected %s' % selectOption)
            print(name + ' how much would you like to withdrawl today?')
            amount = input('')
            print('You selected ' + amount + ' is this correct?')
            first_respone = 'yes'
            response = input('')
            if(response =='yes'):
                print('Have a great day and thanks for choosing Chase Bank!')
                returnres = input('Would you like to return to the main menu? ' )
                if(returnres == 'yes'):
                    print('These are the available options.')
                    print('1. Withdrawl')
                    print('2. Deposit')
                    print('3. Complaint')
                    selectOption = int(input('Please select an option:'))
                    print('You selected %s' % selectOption)

                    
            elif(returnres =='no'):
                    print('Please renter the amount that you need.')

        
        elif(selectOption == 2):
            print('You selected %s' % selectOption)
            print('Please insert cash.')
            cash = input('How much cash did you enter: ')
        
            print(cash + " is the amount that is displayed on the screen correct?")
            
            correct_cash = input('')
            if(correct_cash == 'yes'):
                print('Have a great day, and thanks for choosing Chase Bank!')
            elif(correct_cash == 'no'):
                print('Please renter the cash.')
                print('Please insert cash.')
                cash = input('How much cash did you enter: ')
                print(cash + " is the amount that is displayed on the screen correct?")
                correct_cash = input('')
                if(correct_cash == 'yes'):
                    print('Have a great day, and thanks for choosing Chase Bank!')
                elif(correct_cash == 'no'):
                    print('Please renter the cash.')
                    
                    
                    
                    
                    
            
            
            
            
        elif(selectOption == 3):
            print('You selected %s' % selectOption)
            complaint = ''
            complaint = input('Please enter your complaint? ' )
            input('You entered ' + complaint + ' is this correct? ' )
            if(complaint):
                print('We do apologize for the inconvenience, our customercare team will be in contact with you within the next 24 hours. Have a great day, and thanks for choosing Chase Bank ')
            
        else: 
            print('Invalid option selected, please try again.')
    else:
        print('Password incorrect, please try again.')

else:
    print('Name is not found, please try again.')







