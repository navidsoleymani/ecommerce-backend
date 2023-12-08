from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=50)
    url_title = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',
                               on_delete=models.CASCADE)
    level = models.IntegerField()
    is_head = models.BooleanField()
    is_teal = models.BooleanField()
    is_mead = models.BooleanField()

    class Meta:
        db_table = 'product_category'


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'brand'


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.BigIntegerField()
    short_description = models.TextField()
    description = models.TextField()
    is_special = models.BooleanField()
    is_exist = models.BooleanField()
    count = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    discount_price = models.BigIntegerField(default=0)
    product_detail = models.JSONField()

    class Meta:
        db_table = 'product'


class Comment(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',
                               on_delete=models.CASCADE)
    product = models.BigIntegerField()
    user = models.BigIntegerField()
    text = models.TextField()

    class Meta:
        db_table = 'comment'


class ProductGallery(models.Model):
    image_name = models.CharField(max_length=50)
    image_slug = models.SlugField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_gallery'

