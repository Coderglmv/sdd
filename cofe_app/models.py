from distutils.text_file import TextFile
from django.db import models
from django.forms import CharField, ImageField

# Create your models here.


class MainPage(models.Model):
    image = models.ImageField(upload_to='media/uploads')
    title = models.CharField(max_length=400)
    body  = models.TextField()
    about_us_product = models.CharField(max_length=200)
    video = models.FileField(upload_to='media/uploads')

class MainAboutProduct(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)    


class Connection(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length = 254)
	phone = models.IntegerField()
	special_request = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

class About_us(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

class Mini_aboutUs(models.Model):
    body = models.TextField()    


class Products(models.Model):
    image = models.ImageField(upload_to='media/uploads')
    price = models.CharField(max_length=20)
    money = models.CharField(max_length=10)
    old_price = models.CharField(max_length=100, null=True, blank=True)
    about_product = models.TextField(null=True, blank=True)
    return_policy = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    
