from django.contrib import admin
from . models import Product  # Offers #import the offer class
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

# name convention:- modelnameAdmin 

# class OffersAdmin(admin.ModelAdmin):  #now create a new class offer admin

#     list_display = ('codea','discout')

admin.site.register(Product, ProductAdmin)
# admin.site.register(Offers, OffersAdmin)