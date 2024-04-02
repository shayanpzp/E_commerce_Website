# from enum import unique
# from pyexpat import model
# from sys import prefix
# from pyparsing import alphas   

from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from product.models import Product
from customer.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
 
 
STATUS_CHOICE = (
     ("process", "Processing"),
     ("shipped", "Shipped"),
     ("delivered", "Delivered"),
 )


STATUS = (
     ("draft", "Draft"),
     ("disable", "Disable"),
     ("rejected", "Rejected"),
     ("in_review", "In Review"),
     ("published", "Published"),
 )


RATING = (
     (1, "⭐"),
     (2, "⭐⭐"),
     (3, "⭐⭐⭐"),
     (4, "⭐⭐⭐⭐"),
     (5, "⭐⭐⭐⭐⭐"),
 )
 
 
def user_directory_path(instance, filename):
     return 'user_{0}/{1}'.format(instance.user.id, filename)
    

class Tags(models.Model):...


class CartOrder(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

    
    class Meta:
        verbose_name_plural = "Cart Order"


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=1000, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=1000, decimal_places=2, default="1.99")
    
    
    class Meta:
        verbose_name_plural = "Cart Order Items"
        
        
    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image.url))

    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    
    
    class Meta:
        verbose_name_plural = "Wishlists"
        
    def __str__(self):
        return self.product.title
             
              
              
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mobile = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Address"
    

   



