from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    category_product = models.ForeignKey('CategoryProduct', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CategoryProduct(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=24, default=None)

    def __str__(self):
        return self.name


# Create your models here.
