from django.db import models

# Create your models here.
class Food(models.Model):
    barcode = models.CharField(primary_key=True,max_length=20)
    foodName = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)