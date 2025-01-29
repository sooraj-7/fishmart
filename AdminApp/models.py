from django.db import models

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images',default='null.jpg')

class product(models.Model):
    name1=models.CharField(max_length=20)
    description1=models.CharField(max_length=50)
    price1=models.IntegerField()
    categories=models.CharField(max_length=20,default="")
    image1=models.ImageField(upload_to='images',default='null.jpg')
