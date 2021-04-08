#\n = drops to the next line

name = input('What is your name? \n')
allowedUsers = ['Jalen', 'Mike', 'Tony', 'Lisa']
allowedPassword = ['PasswordJalen', 'PasswordMike', 'PasswordTony', 'PasswordLisa']
import random
from datetime import date
today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print( d1)

from datetime import datetime
now = datetime.now()
print(now)

database = {}

def complaint(selectOption):
    print('You selected %s' % selectOption)
    complaint = ''
    complaint = input('Please enter your complaint? ' )
    input('You entered ' + complaint + ' is this correct? ' )
    if(complaint):
        print('We do apologize for the inconvenience, our customercare team will be in contact with you within the next 24 hours. Have a great day, and thanks for choosing Chase Bank ')
        main()
            

def Deposit(selectOption):
    print('You selected %s' % selectOption)
    print('Please insert cash.')
    cash = input('How much cash did you enter: ')
    print(cash + " is the amount that is displayed on the screen correct?")
                
    correct_cash = input('')
    if(correct_cash == 'yes'):
        print('Have a great day, and thanks for choosing Chase Bank!')
        main()
    elif(correct_cash == 'no'):
        print('Please renter the cash.')
        print('Please insert cash.')
        cash = input('How much cash did you enter: ')
        print(cash + " is the amount that is displayed on the screen correct?")
        correct_cash = input('')
        if(correct_cash == 'yes'):
            print('Have a great day, and thanks for choosing Chase Bank!')
            main()
        elif(correct_cash == 'no'):
            print('Please renter the cash.')
        

def Withdrawl(selectOption):
    print('You selected %s' % selectOption)
    print(name + ' how much would you like to withdrawl today?')
    amount = input('')
    print('You selected ' + amount + ' is this correct?')
    first_respone = 'yes'
    first_response = input('')
    if(first_response =='yes'):
        print('Have a great day and thanks for choosing Chase Bank!')
        returnres = input('Would you like to return to the main menu?')
        if(returnres == 'yes'):
            main()
        elif(returnres =='no'):
            print('Please renter the amount that you need.')                                
            
        
def main():
    allowedUsers = ['Jalen', 'Mike', 'Tony', 'Lisa']
    allowedPassword = ['PasswordJalen', 'PasswordMike', 'PasswordTony', 'PasswordLisa']
    if(name in allowedUsers):
        password = input('What is  your password? \n')
        userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome  %s' %  name)
        print('These are the available options:' )
        print('1.Register') 
        print('4. Withdrawl')
        print('5. Deposit')
        print('6. Complaint')

        selectOption = int(input('Please select an option:' ))
        print(d1, now)
        userInput = True 
        print(selectOption)
        if(selectOption == 1):
            register()
        elif(selectOption == 4):
            Withdrawl(selectOption) 
        elif(selectOption == 5):
            Deposit(selectOption)
        elif(selectOption == 6):
            complaint(selectOption)
        elif(selectOption != 4, selectOption != 5, selectOption != 6, selectOption): 
            print('Invalid option selected, please try again.')
        
    elif(password  not in allowedPassword):
        print('Password incorrect, please try again.')

    else:
        print('Name is not found, please try again.') 

def depositOperation():
    print('Deposit Operation')

def withdrawlOperation():
    print('withdrawl')

def logout():
    login()

def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))


   
    selected_option = int(input("What would you like to do? (1) Deposit (2) Withdrawl(3) Logout (4) Exit \n" ))

    if(selected_option == 1):
            
        depositOperation()
    elif(selected_option == 2):
            
        withdrawlOperation()
    elif(selected_option == 3):
            
        logout()
    elif(selected_option == 4):
            
        exit()
    else:
            
        print("Invalid option selected")
        bankOperation(user)


def login():
    print('****** Login*********')

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input('What is your password? \n')

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                    
        
        print('Invalid account number or password.')
        login()

def gernerateAccountNumber():
    
    return random.randrange(1111111111, 9999999999)

def register():
    print('***** Register ******')

    email = input('What is your email address? \n')
    first_name = input('What is your First Name? \n')
    last_name = input('What is your Last Name? \n')
    password = input('Create a password \n')

    accountNumber = gernerateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print('Your account has been created.')
    print("== ==== ===== ==== ===")
    print("Your account number is %d" % accountNumber)
    print("Make sure you keep it safe")

    login()         

main()      
            
            
            
            
        




