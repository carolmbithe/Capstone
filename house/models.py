from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class House(models.Model):
    house_image=models.ImageField(upload_to='businesses',null=True)
    house_number=models.CharField(max_length =10)
    tenant=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length =10)


class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='profiles',null=True)
    user_name=models.OneToOneField(User,null=True,on_delete=models.CASCADE,related_name="user")
     # = models.ForeignKey(House,blank=True, on_delete=models.CASCADE,null=True,related_name='comment')

class Receipt(models.Model):
    receipt_image=models.ImageField(upload_to='receipts',null=True)
     # = models.ForeignKey(House,blank=True, on_delete=models.CASCADE,null=True,related_name='comment')
