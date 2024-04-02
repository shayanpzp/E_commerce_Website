from django.contrib import admin
from core.models import  CartOrder, CartOrderItems, Wishlist, Address


    
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['price', 'paid_status', 'order_date', 'product_status']
    list_filter =  ['price' , 'paid_status' , 'product_status']
    
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image', 'quantity', 'price', 'total']
    list_filter =  ['item' , 'quantity' , 'price']


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']
    
    
class AddressAdmin(admin.ModelAdmin):
    list_editable = ['address', 'status']
    list_display = ['user', 'address', 'status']  
    


admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
