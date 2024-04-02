from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from customer.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
 
 
def user_directory_path(instance, filename):
     return 'user_{0}/{1}'.format(instance.user.id, filename)
    
    
class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgh12345")
    
    #base fields
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")
    description = models.TextField(null=True, blank=True, default="بهترین دسته بندی")
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    
    def __str__(self):
        return self.title