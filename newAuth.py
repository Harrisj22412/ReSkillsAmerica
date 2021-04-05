#register 
# - username and password, email address
# - genrate  user account
#- 


#login
#- username or email and password

#bank operations

database = {}

#Initializing the system

def init():
    isValidOptionSelected = False
    print('Welcome to bankPython')

    while isValidOptionSelected ==  False:

        haveAccount = int(input("Do you have an account with us: 1(yes) 2(no) \n"))
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print('You have selected invailed option.')


def login():
    print('This is the login function')

def register():
    print('This is the register function')


def bankOperation():
    print('Some operations')

def gernerateAccountNumber():
    print('Account number generator')


# Actual Banking System

