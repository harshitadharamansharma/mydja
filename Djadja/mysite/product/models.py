from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
# stdard max lenght for img url

# class Offer(models.Model):
#     code = models.CharField(max_length=10)
#     description = models.CharField(max_length=255)
#     discount = models.FloatField()

# class Offers(models.Model):
#     codea = models.CharField(max_length=10)
#     description = models.CharField(max_length=255)
#     discount = models.FloatField()
# #
