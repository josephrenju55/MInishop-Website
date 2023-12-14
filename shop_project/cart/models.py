from django.db import models
from home.models import shop
from django.contrib.auth.models import User, auth

# Create your models here.

class cartlist(models.Model):
    cart_id=models.CharField(max_length=50,unique=True)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.cart_id


class cartitems(models.Model):
    product=models.ForeignKey(shop,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    available=models.BooleanField(default=True)

    def __str__(self):
        return str(self.product)
    
    def total(self):
        return self.product.price*self.quantity
    
class checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    expiry_month = models.CharField(max_length=2)
    expiry_year = models.CharField(max_length=2)
    cvv = models.CharField(max_length=3)
