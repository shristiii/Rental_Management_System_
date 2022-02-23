from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from sys import argv


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50,null=True)
    email = models.URLField(max_length=200,null=True)
    updated_date = models.DateTimeField(auto_now_add=True,null=True)
    book_location = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=200,null=True)
    condition= [
    ('booked', 'booked'),
    ('not_booked', 'not_booked'),
    ('not_booked','not_booked'),
    ]
    status=models.CharField(max_length=12,choices=condition,default='not_verified' )
    rent_no = models.CharField(max_length=50,null=True)
    book_date = models.DateTimeField(null=True)

    

class Info(models.Model):
    rent_no = models.CharField(max_length=50,null=True)
    hotel_Main_Img = models.ImageField(upload_to='images/')
    book_location = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=200,null=True,default="123")
    desc = models.TextField(null=True)
    
class Notify(models.Model):
    f_name = models.CharField(max_length=50,null=True)
    l_name = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=50,null=True)
    message = models.CharField(max_length=500,null=True)
    email = models.URLField(max_length=200,null=True)
    