from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from category.models import Category
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
 
 
 
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven", alphabet="abcdefgh12345")
    
    #ForeignKey
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category") 
    # vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name="product")
    
    #base fields
    title = models.CharField(max_length=100, default="Fresh Pear")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    description = RichTextUploadingField(null=True, blank=True, default="This is the product.")
    
    price = models.DecimalField(max_digits=1000, decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=1000, decimal_places=2, default="2.99")
    
    specifications = RichTextUploadingField(null=True, blank=True)
    type = models.CharField(max_length=100, default="کارکرده", null=True, blank=True)
    stock_count = models.CharField(max_length=100, default="۸ ایتم", null=True, blank=True)
    life = models.CharField(max_length=100, default="100 روز ", null=True, blank=True)
    mfd = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    tags = TaggableManager(blank=True)
    
    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
    
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    digital = models.BooleanField(default=True)
    
    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")
    
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(null=True, blank=True)
    
    
    
    class Meta:
        verbose_name_plural = "Product"
        
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    
    def __str__(self):
        return self.title
    
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price - 100
    
    
    
class ProductImage(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    
    
    class Meta:
        verbose_name_plural = "Product Images"



class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField(choices = RATING, default=None)
    date = models.DateField(auto_now_add=True)
    
    
    class Meta:
        verbose_name_plural = "Product Review"
        
    def __str__(self):
        return self.product.title
        
        
    def get_rating(self):
        return self.rating