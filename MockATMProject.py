#\n = drops to the next line

name = input('What is your name? \n')
allowedUsers = ['Jalen', 'Mike', 'Tony', 'Lisa']
allowedPassword = ['PasswordJalen', 'PasswordMike', 'PasswordTony', 'PasswordLisa']




if(name in allowedUsers):
    password = input('What is  your password? \n')
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome  %s' %  name)
        print('These are the available options:')
        print('1. Withdrawl')
        print('2. Deposit')
        print('3. Complaint')

        selectOption = int(input('Please select an option:'))
        userInput = True 
        print(selectOption)
        if(selectOption == 1):
            print('You selected %s' % selectOption)
            print(name + ' how much would you like to withdrawl today?')
            amount = input('')
            print('You selected ' + amount + ' is this correct?')
            first_respone = 'yes'
            input('')
            if('yes'):
                print('Have a great day and thanks for choosing Chase Bank!')
            else:
                print('Please renter the amount that you need.')

        
        elif(selectOption == 2):
            print('You selected %s' % selectOption)
            print('Please insert cash.')
            cash = input('')
        
            print(cash + " is the amount that is displayed on the screen correct?")
            member_response = 'yes'
            input('')
            if(cash == 'yes'):
                print('Have a great day, and thanks for choosing Chase Bank!')
            else:
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







