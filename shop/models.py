from django.db import models
from django.db.models.base import ModelState
import uuid
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100) 
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    detail = models.TextField()
    image = models.ImageField('image', upload_to='Product/image')

    def __str__(self):
        return f"{self.name}-{self.category}"