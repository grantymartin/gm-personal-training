from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

# Create your tests here.
class TestAccountForms(TestCase):
    
    def test_user_login_form_only_username(self):
        form = UserLoginForm({'username':'testing'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])
        
    def  test_user_login_form_all_filled(self):
        form = UserLoginForm({'username':'testing','password':'1212121212'})
        self.assertTrue(form.is_valid())
    
    def test_user_registration_form_only_email(self):
        form = UserRegistrationForm({'email':'testing'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])
        
    def  test_user_registration_form_all_filled(self):
        form = UserRegistrationForm({'email':'testing@msn.com','username':'usertest','password1':'testing121!','password2':'testing121!'})
        self.assertTrue(form.is_valid())
    
    def  test_user_registration_form_all_filled_faulty_email(self):
        form = UserRegistrationForm({'email':'testingmsn.com','username':'usertest','password1':'testing121!','password2':'testing121!'})
        self.assertFalse(form.is_valid())
        
    def  test_user_registration_form_all_filled_faulty_passwords(self):
        form = UserRegistrationForm({'email':'testing@msn.com','username':'usertest','password1':'testing121!','password2':'testing'})
        self.assertFalse(form.is_valid())