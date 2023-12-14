from django.db import models
from django.urls import reverse

# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    
    def __str__(self):
        return '{}'.format(self.name)
    
    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

class shop(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    stock=models.IntegerField()
    img=models.ImageField(upload_to='product')
    cate=models.ForeignKey(categ,on_delete=models.CASCADE)
    available=models.BooleanField()
    price=models.IntegerField()
    desc=models.TextField()
    date=models.DateTimeField()