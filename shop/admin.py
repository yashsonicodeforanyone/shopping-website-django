from django.contrib import admin

# Register your models here.
from . models import Product,Contact,Order,orderupdate
from .models import Item
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(orderupdate)


