from django.db import models
import datetime as dt

from django.contrib.auth.models import User


# Create your models here.

class House(models.Model):
    house_image=models.ImageField(upload_to='businesses',null=True)
    house_number=models.CharField(max_length =10)
    tenant=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length =10)

    def __str__(self):
        return self.house_number


class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='profiles',null=True)
    user_name=models.OneToOneField(User,null=True,on_delete=models.CASCADE,related_name="user")
    email = models.EmailField(null=True,blank=True)
    phone_number = models.CharField(max_length = 10,blank = True)


    def __str__(self):
        return self.user_name

class Receipt(models.Model):
    receipt_image=models.ImageField(upload_to='receipts',null=True)
    profile=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    upload_time=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    room_number= models.ForeignKey(House,blank=True, on_delete=models.CASCADE,null=True,related_name='house')

    

class Post(models.Model):
    title=models.CharField(max_length =30)
    post=models.TextField(blank=True,null=True)
    upload_time=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.title
