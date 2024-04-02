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
 
 
 
class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven", alphabet="abcdefgh12345")
    
    #base fields
    title = models.CharField(max_length=100, default="Apple-nic")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    cover_image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    description = RichTextUploadingField(null=True, blank=True, default="I am a amazing vendor.")
    
    address = models.CharField(max_length=100, default="123 Main Street.")
    contact = models.CharField(max_length=100, default="+123 (456) 789")
    chat_resp_time = models.CharField(max_length=100, default="88")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")
    
    #ForeignKey
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    mall = models.CharField(max_length=100, default="مرکز خرید")
    
    class Meta:
        verbose_name_plural = "Vendors"
        
    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    
    def __str__(self):
        return self.title
    
    
    
    