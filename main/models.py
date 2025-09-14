
from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('tas', 'Tas'),
        ('bola', 'Bola'),
        ('sepatu', 'Sepatu'),
        ('baju', 'Baju'),
        ('general', 'General')
    ]
    
    name = models.CharField(max_length=255, primary_key=True)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="general")
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=50, default="Unknown")
    rating = models.DecimalField(default=0.0, max_digits=5, decimal_places=1)
    
def __str__(self):
    return self.title