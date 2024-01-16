from django.contrib import admin
from customer.models import User



class USerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']


admin.site.register(User, USerAdmin)