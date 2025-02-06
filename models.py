from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    ProductType = models.TextChoices("ProductType", "INSTRUMENT ACCESSORY MUSIC")
    product_type = models.CharField(blank=True, choices=ProductType, max_length=10)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="media/aria_music")
    date_rec = models.DateTimeField("date received")
    
    def __str__(self):
        return self.sku + " : " + self.name
    

