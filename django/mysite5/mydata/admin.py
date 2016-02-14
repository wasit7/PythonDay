from django.contrib import admin
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price']

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','time','product','customer','quantity']    

admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)