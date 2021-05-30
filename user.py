class User:
    """
   class that creaes an instance of a class

    """

    user_list=[]

    def __init__(self,username):
        self.username= username
    
    def save_user(self):
        """
        create method to save usersane
        """

        User.user_list.append(self)

     
class Credentials:
    """
    create a class that create instance of the class

    """
    credentials_list = []

    def __init__(self,password):
        self.password = password

    def save_user_password(self):
        """method to save the  use password"""
        Credentials.credentials_list.append(self)
    @classmethod
    def display_credentials(cls):
        """
        function to display user display_credentials
        """


    




