from atexit import register
from django.contrib import admin

from market.models import  Product, Category


# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')



admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
