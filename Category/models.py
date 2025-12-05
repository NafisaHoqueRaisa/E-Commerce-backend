from django.db import models

# Create your models here.
class Category (models.Model):
    name= models.CharField(max_length=50)
    image= models.ImageField(upload_to="Category/image/")
    slug=  models.SlugField(max_length=40)

    def __str__(self):
        return self.name
   
