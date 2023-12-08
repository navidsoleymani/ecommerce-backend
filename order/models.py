from django.db import models

from product.models import Product
from users.repo.models.user import User


class Order(models.Model):
    STATE_CHOICES = [
        ('P', 'pending'),
        ('A', 'accept'),

    ]
    delivery_price = models.BigIntegerField()
    total_price = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paymentDate = models.DateTimeField()
    state = models.CharField(choices=STATE_CHOICES, max_length=1, default='p')
    discount_price = models.BigIntegerField()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    price = models.BigIntegerField()

    class Meta:
        db_table = 'order_detail'


class Payment(models.Model):
    payment_date = models.DateTimeField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_number = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'payment'


class Delivery(models.Model):
    STATUS_CHOICES = [
        ('p', 'process'),
        ('s', 'sent'),
        ('c', 'cancel'),
        ('d', 'delivered')
    ]
    TYPE_CHOICES = [
        ('s', 'ship'),
        ('a', 'airplane'),
        ('c', 'car')
    ]
    delivery_status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='p')
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_type = models.CharField(choices=TYPE_CHOICES, max_length=1, default='c')

    class Meta:
        db_table = 'delivery'

