
from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField
    description = models.TextField
    thumbnail = models.URLField
    category = models.CharField
    is_featured = models.BooleanField
    brand = models.CharField
    rating = models.DecimalField(default=0.0, max_digits=5, decimal_places=1)
    
def __str__(self):
    return self.title