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
    


