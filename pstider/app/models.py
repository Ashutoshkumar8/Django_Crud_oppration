from django.db import models

# Create your models here.

class Croud(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField(default=0)
    sal=models.FloatField(max_length=30)
