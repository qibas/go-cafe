from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    name_person = models.CharField(max_length=255)
    class_name = models.TextField()
    npm = models.IntegerField()
