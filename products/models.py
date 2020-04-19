from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    CATEGORIES = [
        ('M', 'Men'),
        ('W', 'Women'),
        ('E', 'Equipment'),
    ]
    categories = models.CharField(max_length=1, choices=CATEGORIES, default=True)

    def __str__(self):
        return self.name