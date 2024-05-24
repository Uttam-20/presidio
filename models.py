from django.db import models
import members
class Seller(models.Model):
    name=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=10)
    addr=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
class Buyer(models.Model):
    name=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=10)
    status=models.CharField(max_length=255)
class Selling(models.Model):

    Hno=models.IntegerField()
    Hadrr=models.CharField(max_length=255)
    Htype=models.CharField(max_length=255)
    rooms=models.IntegerField()
    Himg=models.ImageField(upload_to='members/static/images')
    Contact=models.CharField(max_length=10)
class Buying(models.Model):
    name=models.CharField(max_length=255)
    Htype=models.CharField(max_length=255)
    rooms=models.IntegerField()
    Hplace=models.CharField(max_length=255)
    mobile=models.CharField(max_length=10)

