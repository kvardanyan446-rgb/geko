from django.db import models

class Product(models.MOdel):
    name = models.CharField(max_length=100)
    