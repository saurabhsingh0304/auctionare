from django.contrib import admin
from .models import VendorUser, BidderUser

# Register your models here.

admin.site.register(VendorUser)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('first_name' , 'last_name' , 'email' , 'mobile' , 'city' , 'postal_code' , 'country')
    list_filter = ('country', 'city' ,)
    search_fields = ('first_name' , 'last_name', 'city' , 'postal_code' , 'country')

admin.site.register(BidderUser)
class BidderAdmin(admin.ModelAdmin):
    list_display = ('first_name' , 'last_name' , 'email' , 'mobile' , 'city' , 'postal_code' , 'country')
    list_filter = ('country', 'city' ,)
    search_fields = ('first_name' , 'last_name', 'city' , 'postal_code' , 'country')
