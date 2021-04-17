#register 
# - first name, last name, password, email address
# - genrate  user account
#- 


#login
#- first name, last name or email and password

#bank operations

#Initializing the system
import random 

database = {}

#Initializing the system

def init():
    
    print('Welcome to bankPython')

    haveAccount = input("Do you have an account with us: 1 (yes) 2 (no) \n")
    if(haveAccount == 1):
        login()
    elif(haveAccount == 'no'):
        print(register())
    else:
        print('You have selected invailed option.')
        init()


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

def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))


   
    selected_option = int(input('What would you like to do? (1) Deposit (2) Withdrawl (3) Logout (4) Exit \n' ))

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



def withdrawlOperation():
    print('withdrawl')

def depositOperation():
    print('Deposit Operation')


def gernerateAccountNumber():
    
    return random.randrange(1111111111, 9999999999)

def logout():
    login()



# Actual Banking System

gernerateAccountNumber()

init()


