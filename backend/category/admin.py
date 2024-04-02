from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']
    

admin.site.register(Category, CategoryAdmin)

