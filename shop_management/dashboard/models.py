from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name
