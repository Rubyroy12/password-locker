from user import User,Credentials


def create_account(self,new_username,password,confirm_password):
    """create  new user account"""

    new_account = User(username, password,confirm_password)

    return new_account
    
def save_user(user):
    """Save user details
    """
    return user.save_user()
def delete_user(self):
    """
    method to delete_user details

    """
    User.user_list.remove(self)

def create_new_credential(account,username,password):
    """
    function that create new credential details for a new user
    """
    new_credential = Credentials(account,username,password)
    return new_credential

def save_user_details(credentials):
    """method to save the  use password"""
    credentials.credentials_list.append()

def delete_user_credentials(credentials):
    """delete user credentials"""

    credentials.credentials_list.remove()
def generate_password(self):
    """
    a function that generates password randomly
    """
    auto_password = Credentials.generate_password(self)
    return auto_password


def main():
    """main function to process user requests."""

while True:
    print("Wecome to password locker")
    print("___________________")
    print('\n')

    print("welcome, type 'new' to create a new password locker or 'login' to login to your existing account or 'ex' to exit the application")
    print('\n')
    # print(f"your random password is: {random_password}")
    option= input("Enter your choice: ").lower()
    
    
  
    
    if option=='new':
        print("Enter account name")
        account=input()
       
        print("Enter username")
        new_username = input()

        # password = generate_password(password)
        # print(f"You can you system genrated password {password}")

        print("Create password")
        new_password= input()

        print("Confirm password")
        confirm= input()


        while new_password!= confirm:
            print("password did not match")
            print("Please create password")
            password= input()

            print("Confirm password")
            confirm= input()

            save_user_details(create_account(username,password))
        
        else:
            print("You have successfully created password locker account")
            print("\t\t\t"+'________________'+ "\t\t\t")
            print('\n')
            print("***LOGIN***")
            print('\n')
            print("Enter username")
            username= input()
            print("Enter password")
            password= input()

            while username != new_username or password != new_password:
                print("Invalid credentials")
                print("Enter username")
                username= input()
                print("Enter password")
                password= input()
            else:
                print("Login successfull")
                print("\n")
                print("Vew your details below")

                # print(f"***{username}***")
                # print(f"***{password}***")
    
    elif option =='login':

        print("Welcome : LOGIN ")
        print('\n')

        print('Enter your username:')
        default_username = input()

        print('Enter Password:')
        default_pasword = input()

        print('\n')
        print('You have successfully logged in')
        print("\t\t"+'________________'+ "\t\t")

        while default_username != new_username or default_password != new_password:
            print('Invalid credentials')
            print('Please try again')





    elif option=="ex":
        break
 

if __name__ == '__main__':
    main()