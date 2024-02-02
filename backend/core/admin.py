from django.contrib import admin
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImage, ProductReview, Wishlist, Address



class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['user', 'title', 'product_image', 'price', 'vendor', 'category', 'featured', 'product_status', 'pid']
    list_filter =  ['user' , 'title']
    list_editable = ['vendor']
    sortable_by =  ['price']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']
    
    
class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']
    list_filter =  ['title' ]
    
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'order_date', 'product_status']
    list_filter =  ['price' , 'paid_status' , 'product_status']
    
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image', 'quantity', 'price', 'total']
    list_filter =  ['item' , 'quantity' , 'price']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']
    
    

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']  
    




admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
