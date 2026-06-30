from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    is_avilable = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    quantity = models.IntegerField(default=0)
    description = models.TextField(max_length=255)
    made_in = models.CharField(max_length=20)
