from django.db import models
from AdminApp.models import*

# Create your models here.
class feedback(models.Model):
    email=models.CharField(max_length=100)
    feedbacks=models.CharField(max_length=100)


class register(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    contact1=models.IntegerField()

class cart(models.Model):
    usercart=models.ForeignKey(register,on_delete=models.CASCADE)
    userpro=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0)

class checkout(models.Model):
    usercheckout=models.ForeignKey(register,on_delete=models.CASCADE)
    usercart=models.ForeignKey(cart,on_delete=models.CASCADE)
    address=models.TextField()
    state=models.CharField(max_length=30)
    pincode=models.IntegerField()
    country=models.CharField(max_length=20)





