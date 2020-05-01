from django.test import TestCase
from .forms import OrderForm

# Create your tests here.
class TestOrderForm(TestCase):
    
    def test_order_form_only_full_name(self):
        form = OrderForm({'full_name':'testing'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['phone_number'], ['This field is required.'])
        
    def test_order_form_only_full_name_and_phone_number(self):
        form = OrderForm({'full_name':'testing', 'phone_number':'1212121212'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['country'], ['This field is required.'])
        
    def  test_order_form_all_filled(self):
        form = OrderForm({'full_name':'testing','phone_number':'1212121212','country':'testing','postcode':'testing','town_or_city':'testing','street_address1':'testing','street_address2':'testing','county':'testing'})
        self.assertTrue(form.is_valid())