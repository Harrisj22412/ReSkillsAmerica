def account_number_validation(account_number):
    #check if account_number is not empty
    #if account_number is 10 digits
    #if the account_number is an integer
    if account_number:
        
        try:
            int(account_number)

            if len(str(account_number)) == 10:
                return True

            #else:
                #print("Account Number cannot be more than 10 digits")
                #return False

        except ValueError:
            #print("Invalid Account number, account number should be integer")
            return False

        except TypeError:
            #print("Invalid account type ")
            return False
        
        #print("Account Number is a required field")
    return False

#def validation_registration_input(input):
    #check if it's a list
    #check each item in the list and be sure they are the correct data types