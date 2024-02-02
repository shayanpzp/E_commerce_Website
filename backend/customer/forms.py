from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from customer.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder" : "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Confirm Password"}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Old Password"}),
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={"placeholder": "New Password"}),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm New Password"}),
    )