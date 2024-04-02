from django.contrib import admin
from product.models import Product,  ProductImage, ProductReview



class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['user', 'title', 'product_image', 'price', 'category', 'featured', 'product_status', 'pid']
    list_filter =  ['user' , 'title']
    sortable_by =  ['price']
    

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
