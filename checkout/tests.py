from django.test import TestCase
from .forms import OrderForm
from .models import Order

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

class TestCheckoutModels(TestCase):
    def test_order_models(self):
        order = Order(full_name="1", phone_number="121212121", country="Testing", postcode="", town_or_city="Test Town", street_address1="test street1", street_address2="test street2", county="test vill", date="2020-01-01")
        order.save()
        self.assertEqual(order.postcode, "")
        self.assertNotEqual(order.postcode, "1")
        self.assertEqual(order.street_address1, "test street1")
        self.assertNotEqual(order.street_address1, "test street2")
    
    def test_blank_to_false(self):
        order = Order(full_name="", phone_number="", country="", postcode="", town_or_city="", street_address1="", street_address2="", county="", date="2020-01-01")
        order.save()
        self.assertFalse(order.full_name, "")
        self.assertFalse(order.phone_number, "")
        self.assertFalse(order.country, "")
        self.assertFalse(order.town_or_city, "")
        self.assertFalse(order.street_address1, "")
        self.assertFalse(order.street_address2, "")
        self.assertFalse(order.county, "")