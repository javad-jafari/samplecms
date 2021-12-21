from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth import models
User = get_user_model()


class Basket(models.Model):

    user = models.OneToOneField(User, related_name='baskets', on_delete=models.CASCADE)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField( default=False)

    def __str__(self):
        return self.name




class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, related_name='basketitems', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField( default=1)
    price = models.PositiveIntegerField( default=0)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    

    def __str__(self):
        return self.name
