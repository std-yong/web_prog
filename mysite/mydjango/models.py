from django.db import models

# Create your models here.

class Item(models.Model):
    itemid = models.CharField(max_length=50, primary_key=True)
    itemname = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    pictureurl = models.ImageField(upload_to='images/', blank=True, null=True)
