import unittest
from user import User
from user import Credentials
class Testuser(unittest.TestCase):
    def setUp(self):
        self.new_user_credentials = Credentials("twitter","Ibrahim","Ibra1224")
    def tearDown(self):
        """Tear down"""
        Credentials.credentials_list=[]

    def test_init(self):
        self.assertEqual(self.new_user_credentials.account,"twitter")
        self.assertEqual(self.new_user_credentials.username,"Ibrahim")
        self.assertEqual(self.new_user_credentials.password,"Ibra1224")
    
    def test_save_user_details(self):
        """Save"""
        self.new_user_credentials.save_user_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_delete_user_credentials(self):
        """Delete user"""
        self.new_user_credentials.save_user()
        test_user=Credentials("facebook","John","Doe1234")
        test_user.save_user_details()

        self.new_user_credentials.delete_user_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == "__main__":
    unittest.main()