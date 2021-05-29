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
        username=input()

        print("Create password")
        password= input()

        print("Confirm password")
        confirm= input()

        while password!= confirm:
            print("password did not match")
            print("Please create password")
            password= input()

            print("Confirm password")
            confirm= input()
        
        else:
            print("You have successfully created password locker account")
            break
    

    





if __name__ == '__main__':
    main()