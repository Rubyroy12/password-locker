from user import User

def main():
    """main function to process user requests."""

while True:
    print("Wecome to password locker")
    print("___________________")
    print('\n')

    print("welcome, type 'new' to create a new password locker or 'login' to login to your existing account")
    print('\n')
    option= input("Enter your choice: ").lower()
    
    if option=='new':
        print("Enter username")
        new_username = input()

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
        
        else:
            print("You have successfully created password locker account")
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
                print("Vew your details here:" 'http://angular.io')
                print(f"{username}")
                print(f"{password}")
                break

    else:
        print("\n")
        print("I DID NOT RECOGNIZED YOUR INPUT!!!")





    

    





if __name__ == '__main__':
    main()