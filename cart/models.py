import datetime

from django.utils import timezone

from django.db import models

from product.models import Product
from users.repo.models.user import User


class Coupon(models.Model):
    code = models.CharField(max_length=50)
    amount = models.BigIntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    next_year = str(datetime.date.today() + datetime.timedelta(days=365))
    expiration_date = models.DateTimeField(default=next_year, blank=True)

    class Meta:
        db_table = 'coupon'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cart_price = models.BigIntegerField()
    delivery_price = models.BigIntegerField()
    total_price = models.BigIntegerField()

    class Meta:
        db_table = 'cart_item'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.BigIntegerField()

    class Meta:
        db_table = 'cart'

