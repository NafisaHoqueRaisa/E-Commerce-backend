from django.db import models
from Category.models import Category
# Create your models here.
SIZE_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
]



class Product (models.Model):
    name= models.CharField(max_length=50)
    description= models.TextField()
    image= models.ImageField(upload_to="Product/image/")
    sku= models.CharField(max_length=100)
    price=models.IntegerField()
    oldprice= models.IntegerField()
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    quantity= models.IntegerField()

   
    def __str__(self):
        return self.name