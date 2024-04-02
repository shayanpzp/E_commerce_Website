from django.contrib import admin
from customer.models import User, Profile, Contact



class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']


# class ProfileAdmin(admin.ModelAdmin):
#     list_display=['full_name', 'bio', 'phone']

class ContactAdmin(admin.ModelAdmin):
    list_display=['full_name', 'email', 'subject']

admin.site.register(User, UserAdmin)
# admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contact, ContactAdmin)