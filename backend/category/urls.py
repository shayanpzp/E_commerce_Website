from django.urls import path, include
from .views import (
    CategoryListView, 
    CategoryProductListView,
    
)

app_name = "category"

urlpatterns = [
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/<cid>/", CategoryProductListView.as_view(), name="category_product_list"),

]