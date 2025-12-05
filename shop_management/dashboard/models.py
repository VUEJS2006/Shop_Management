from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    photo = models.ImageField(upload_to="products/",null=True,blank=True)
    unit = models.CharField(max_length=100, null= True, blank=True)

    def __str__(self):
        return self.name
class Shop(models.Model):
     name = models.CharField(max_length=100,null=True,blank=True)
     image = models.ImageField(upload_to="shop",null=True,blank=True)
     phone = models.CharField(max_length=100,null=True,blank=True)
     address = models.CharField(max_length=200,null=True,blank=True)
     remark = models.TextField(null=True)
     created_at = models.DateField(auto_now_add=True,null=True)
     updated_at = models.DateField(auto_now=True)


     def __str__(self):
        return self.name

    
    
