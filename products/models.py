from django.db import models

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('fruits', 'Fruits'),
        ('meat', 'Meat'),
        ('health', 'Health'),
        ('personal', 'Personal'),
        ('organizing', 'Organizing'),
        ('battery', 'Battery'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    photo = models.ImageField(upload_to='product images/')
    price = models.PositiveIntegerField()
    quantity = models.IntegerField()
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
