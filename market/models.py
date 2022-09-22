import types
from unicodedata import name
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5000, default="Natural and pure")
    image_url = models.CharField(max_length=2083, default="https://c.ndtvimg.com/2019-04/dl9g6gn8_bananas_625x300_11_April_19.jpg")

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='Grocery')
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)



    def __str__(self):
        return self.name + ' | ' + str(self.category)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')