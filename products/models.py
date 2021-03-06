from django.db import models

CATEGORIES = [('M', 'Mens'),('W', 'Womens'),('E', 'Equipment')]

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    categories = models.CharField(max_length=254, choices=CATEGORIES, default='')

    def __str__(self):
        return self.name
