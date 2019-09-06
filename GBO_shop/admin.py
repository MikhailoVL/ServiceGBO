from django.contrib import admin
from .models import Product, CategoryProduct, Manufacturer


admin.site.register(Product)
admin.site.register(CategoryProduct)
admin.site.register(Manufacturer)

# Register your models here.
