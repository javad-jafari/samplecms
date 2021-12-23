from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product
User = get_user_model()


class Basket(models.Model):

    user = models.OneToOneField(User, related_name='baskets', on_delete=models.CASCADE)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField( default=False)
    basket_price = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    def total_price(self):
        sum = 0
        for item in self.basketitems.all():
            sum += item.price * item.quantity
        return sum




class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, related_name='basketitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='basketitems', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField( default=1)
    price = models.PositiveIntegerField( default=0)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def product_price(self):
        return self.price * self.quantity
    

    def __str__(self):
        return str(self.price)
