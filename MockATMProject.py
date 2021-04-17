#\n = drops to the next line

#!!Please make sure you use the same email address through out this program or you may receive an error message. Thanks!

name = input('What is your name? \n')
#check if name is a string
#check to make sure that the string is greater than one
email = input('Please enter your email address. \n')
#check to make sure that the string is greater than one
#check if email is a string
allowedUsers = ['Jay', 'Mike', 'Tony', 'Lisa']
allowedPassword = ['PasswordJalen', 'PasswordMike', 'PasswordTony', 'PasswordLisa']
people = {'Tom':730, 'Brad':650, 'Steve':710}
#balance = [234, 532, 422, 0]
counter = 3
database_user = {
    'Jalen': 'PasswordJalen',
    'Mike' :  'PasswordMike',
    'Love' : 'PasswordLove'
}


import random
import validation
import database
from getpass import getpass


from datetime import date
today = date.today()

#current time
import time
current = time.localtime()
current_time = time.strftime("%H:%M")
print(current_time)


# dd/mm/YY
d1 = today.strftime("%B %d, %Y")
print( d1)

from datetime import datetime
now = datetime.now()
#print(now)






def complaint(selectOption):
    print('You selected %s' % selectOption)
    complaint = ''
    complaint = input('Please enter your complaint? \n' )
    complaint_response = input('You entered ' + complaint + '. Is this correct? \n' )
    if(complaint_response == 'yes'):
        print('We do apologize for the inconvenience, our customercare team will be in contact with you within the next 24 hours. Have a great day, and thanks for choosing Chase Bank ')
        print(d1)
        print(current_time)
        main()

        
#def get_current_balance(user_details):
    #return  user_details[4]


def account_number_validation(account_number):
    #check if account_number is not empty
    #if account_number is 10 digits
    #if the account_number is an integer
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid Account number, account number should be integer")
                return False
            except TypeError:
                print("Invalid account type ")
                return False


        else:
            print("Account Number cannot be more than 10 digits")



    else:
        print("Account Number is a required field")
        return False



def update_balance():
    global balance
    print('This is your current balance')
    print(balance)
    print(current_time)
    print(d1)
    main()

def lockedOut():
    global counter
    while counter > 1:
        print('Please try again')
        counter = counter - 1

    else:
        print('You have been locked out')
    

def creditCard(people):
    for member in people:
        if people[member] > 700:
            print('Approved', member, people[member])
                
        else:
            print("Decline", member, people[member])

#def set_current_balance(user_details, balance):
    #user_details[4] = balance


def Deposit(selectOption):
    global balance
    print('You selected %s' % selectOption)
    print('Please insert cash.')
    cash = input('How much cash did you enter: ')
    print(cash + " is the amount that is displayed on the screen correct?")
                
    correct_cash = input('')
    if(correct_cash == 'yes'):
        cash = int(cash)
        balance = cash + balance
        new_balance = str(balance)
        print('This is your new balance ' + new_balance)
        print(d1)
        print('Have a great day, and thanks for choosing Chase Bank!')
        main()
    elif(correct_cash == 'no'):
        print('Please renter the cash.')
        
        cash = input('How much cash did you enter: ')
        print(cash + " is the amount that is displayed on the screen correct?")
        correct_cash = input('')
        if(correct_cash == 'yes'):
            print('Have a great day, and thanks for choosing Chase Bank!')
            main()
        elif(correct_cash == 'no'):
            print('Please renter the cash.')
        

def Withdrawl(selectOption):
    global balance
    print('You selected %s' % selectOption)
    print(name + ' how much would you like to withdrawl today?')
    amount = input('')
    new_amount = int(amount)
    print('You selected ' + amount + ' is this correct?')
    #get current balance
    #check if current balance > withdraw balance
    #deduct withdrawn amount amount from current balance
    #display current balance
    
    first_response = input('')
    if(first_response =='yes'):
        balance =  balance - new_amount
        print('This is your new balance.')
        print(balance)
        print(current_time)
        print(d1)
        print('Have a great day and thanks for choosing Chase Bank!')
        returnres = input('Would you like to return to the main menu?')
        if(returnres == 'yes'):
            main()
        elif(returnres =='no'):
            print('Please renter the amount that you need.')                                

        
def main():
    counter = 3
    global name
    global password
    global balance
    allowedUsers = ['Jalen', 'Mike', 'Tony', 'Lisa']
    allowedPassword = ['PasswordJalen', 'PasswordMike', 'PasswordTony', 'PasswordLisa']
    if(name in allowedUsers):
        password = input('What is  your password? \n')
        userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome  %s' %  name)
        print('These are the available options:' )
        print('1.Register')
        print('2. Change Password') 
        print('3. Update Address')
        print('4. Withdrawl')
        print('5. Deposit')
        print('6. Complaint')
        print('7. Balance')
        print('8. Credit Card Application')

        selectOption = int(input('Please select an option: \n' ))
        #check if selectOption is a integer
        print(current_time)
        print(d1 )
        print(selectOption)
        if(selectOption == 1):
            register()
        elif(selectOption == 2):
            changePassword()
        elif(selectOption == 3):
            updateAddress()
        elif(selectOption == 4):
            Withdrawl(selectOption) 
        elif(selectOption == 5):
            Deposit(selectOption)
        elif(selectOption == 6):
            complaint(selectOption)
        elif(selectOption == 7):
            update_balance()
        elif(selectOption == 8):
            creditCard(people)
        elif(selectOption != 4, selectOption != 5, selectOption != 6, selectOption): 
            print('Invalid option selected, please try again.')
        
    elif(password  not in allowedPassword):
        lockedOut()
        
    else:
        print('Name is not found, please try again or select change password option')
         

def changePassword():
    
    secure_code_generator = random.randrange(1111, 9999)
    print(secure_code_generator)
    verify = input("Can you please verify your email address please? \n")
    if (email == verify):
        
        print("A code was sent to your email address")
        usercode = input('Please enter code: \n')

        if(secure_code_generator == int(usercode)):
            print('Your code was accepted and you may now login')
    main()
        #Just a demo for verification and generating a code. 
        


def updateAddress():
    verify_password = input('Please verify your password \n')
    if(verify_password == allowedPassword[0]):
        print('Password was correct!')
        new_address = input('Please enter new address \n')
        is_correct = input('The new address you have entered is' +  new_address + 'is this correct \n')
        if(is_correct == 'yes'):
            print('Your ' + new_address + 'has been updated and you may go back to the main menu.')
            main()
        elif(is_correct == 'no'):
            updateAddress()



def depositOperation():
    print('Deposit Operation')

def withdrawlOperation():
    print('withdrawl')

def logout():
    login()

def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))

    selectOption = int(input('Please select an option: \n' ))
    #check if selectOption is a integer
    print(selectOption)
    if(selectOption == 1):
        register()
    elif(selectOption == 2):
        changePassword()
    elif(selectOption == 3):
        updateAddress()
    elif(selectOption == 4):
        Withdrawl(selectOption) 
    elif(selectOption == 5):
        Deposit(selectOption)
    elif(selectOption == 6):
        complaint(selectOption)
    elif(selectOption == 7):
        update_balance()
    elif(selectOption == 8):
        creditCard(people)
    elif(selectOption != 4, selectOption != 5, selectOption != 6, selectOption): 
        print('Invalid option selected, please try again.')
    else:
        print('Name is not found, please try again or select change password option')
        bankOperation(user)


    



def login():
    print('****** Login*********')

    accountNumberFromUser = input("What is your account number? \n")
    is_valid_account_number = validation.account_number_validation(accountNumberFromUser)

    if is_valid_account_number:

        #password = input('What is your password? \n')
        password = getpass('What is your password \n')
        #check if password is a string

        user = database.authenticated_user(accountNumberFromUser, password)

        if user:
            bankOperation(user)

        #for accountNumber,userDetails in database.items():
            #if(accountNumber == int(accountNumberFromUser)):
                #if(userDetails[3] == password):
                    #bankOperation(userDetails)
                    
        print('Invalid account or password')
        login()

    else:
        print('Invalid Account Number: check that you have up to 10 digits and only integers.')
        main()
        #login()
    
        

def gernerateAccountNumber():
    
    return random.randrange(1111111111, 9999999999)

def register():
    print('***** Register ******')

    email = input('What is your email address? \n')
    first_name = input('What is your First Name? \n')
    #check if name is a string
    #check to make sure that the string is greater than one
    last_name = input('What is your Last Name? \n')
    password = getpass('Create a password for yourself \n')
    #check if name is a string
    #check to make sure that the string is greater than one

    password = input('Create a password \n')
    #check to make sure that password is greater than seven characters

    
    #He deleted in the video and stated that we may not need this
    #try:
    accountNumber = gernerateAccountNumber()

    #except:
        #print('Account generation failed due to system error.')
        #main()



    #database[accountNumber] = [first_name, last_name, email, password, 0]
    

    is_user_created = database.create(accountNumber, first_name + "," + last_name + ','+ email + ',' + password )

    if is_user_created:
        print('Your account has been created.')
        print("Your account number is %d" % accountNumber)
        print("Make sure you keep it safe")

        login()    

    else:
        print('Something went wrong please try again. ')
        register()

    
    print("Something went wrong, please try again")  
    register()   

main()      
            
            
            
            
        




