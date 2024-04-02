from django.contrib import admin
from vendor.models import  Vendor



class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']
    list_filter =  ['title' ]
    
    
admin.site.register(Vendor, VendorAdmin)
