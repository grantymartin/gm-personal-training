from django.test import TestCase
from .models import Product

class ProductTests(TestCase):

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')

class TestProductViews(TestCase):
    def test_Product_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page,"base.html")
        
class TestProductModels(TestCase):
    def test_description_defaults_to_false(self):
        product = Product(name="1", price=1.00, categories="Mens")
        product.save()
        self.assertEqual(product.name, "1")
        self.assertFalse(product.description, "")
        self.assertTrue(product.categories, "Mens")
        
    def test_categories_defaults_to_false(self):
        product = Product(name="1", description="test", price=2.00)
        product.save()
        self.assertNotEqual(product.price, 1)
        self.assertFalse(product.categories, "")
        