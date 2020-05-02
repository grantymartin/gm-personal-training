from django.test import TestCase
from .forms import Email_form

# Create your tests here.
class TestClassesForm(TestCase):
    
    def test_classes_form_only_name(self):
        form = Email_form({'your_name':'testing'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['your_email'], ['This field is required.'])
        
    def  test_classes_form_all_filled(self):
        form = Email_form({'your_name':'testing','your_email':'youremail@msn.com','your_request':'testing'})
        self.assertTrue(form.is_valid())
        