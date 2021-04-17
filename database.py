# create record
#update record
#read record
#delete record
#This is called the crowd operation. 

#search for user

#os allows us to delete a file
import os
import validation


user_db_path = "data/user_record/"

def create(user_account_number,first_name, last_name, email, password):
    user_data = first_name + "," + last_name + ','+ email + ',' + password + ',' + str(0)

    if does_account_number_exist(user_account_number):
        return False

    if does_email_exist(email):
        print("User already exists")
        return False
    
    complention_state = False

    try:
        f = open(user_db_path + str(user_account_number) + '.txt', 'x')
        

    except FileExistsError:
        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not  does_file_contain_data:
            delete(user_account_number)
        #check content of file before deleting
        #delete(account_number)
        # delete the already created file, and print out error, then return false
        #return complention_state
        

    else:
        f.write(str(user_data));
        complention_state = True
        
    finally:
        #anything that happens in finally , will still run
        f.close()
        return complention_state


    #create a new file
    #the name of the file would be account_number.text
    #add the user details to the file
    #return true
    #if saving to file fails, then delete created file

def read(user_account_number):
    #print('read user record')
    #find user with account number
    #fetch content of the file
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + '.txt', 'r')
        else:
            f = open(user_db_path + user_account_number, 'r')

    except FileNotFoundError:
        print('User not found')

    except FileExistsError:
        print("User doesn't exist")

    except TypeError:
        print('Invalid account number format. ')


    else:
        return f.readline()

    return False
    

    
        

def update(user_account_number):
    print('update user record')
    #find user with account number
    #fetch the content of the file
    #update the content of the file
    #save the file
    #return True



def delete(user_account_number):
    #print('delete user record')

    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + '.txt'):
        try:
            os.remove(user_db_path + str(user_account_number) + '.txt')
            is_delete_successful = True

        except FileNotFoundError:
            
            print('User not found')
            

        finally:
            return is_delete_successful


        
    #find user with account number
    #delete the user record which is actually the (file)
    #return True

def does_email_exist(email):
    
    #find user record in the data folder
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
        #print('user printed -->')
        #print(user)
    return False


def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        if user == str(account_number) + '.txt':
            return True
    return False

def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):

        
        user =  str.split(read(account_number), ',')
        
        if password == user[3]:
            return user

    return False

#Instead of an array, list make a dictornary 
#create(1621998871, ['Jalen', 'Harris', 'harrisj22412@hocking.edu', 'PasswordJalen', 500])

#print(read(1621998871))
#does_email_exist(1621998871, 'harrisj22412@hocking.edu')

#print(read({'One', 'Two'}))