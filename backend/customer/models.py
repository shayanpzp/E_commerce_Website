from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager



class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
    

class Profile(models.Model):...
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to="image")
    # full_name = models.CharField(max_length=200, null=True, blank=True)
    # bio = models.CharField(max_length=200, null=True, blank=True)
    # phone = models.CharField(max_length=200)
    # verified = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return self.full_name

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    massage = models.TextField()
    
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
    
    def __str__(self):
        return self.full_name


class ForgetPassword(models.Model):...
