from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
def add(a,b):
    return a+b

class UserTest(TestCase):
    
    # def test_add(self):
    #     self.assertEqual(add(4,5),9)
        
    def setUp(self):
        self.user=User.objects.create(
            username="TestUser",
            first_name="TestFname",
            last_name="TestLname",
            email="testuser123@gmail.com",
            password="User@321"
        )
    def test_user(self):
        user=User.objects.get(username="TestUser")
        self.assertEqual(user.username,self.user.username)
        
    def test_update_user(self):
        user=User.objects.get(username="TestUser")
        old_email=user.email
        user.email="textuxer123@gmail.com"
        user.save()
        user=User.objects.get(username="TestUser")
        self.assertNotEqual(old_email,user.email)