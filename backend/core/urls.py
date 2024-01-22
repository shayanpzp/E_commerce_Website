from django.urls import path
from core.views import index, category_list_view, product_list_view

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("category/", category_list_view, name="category_list"),
    path("products/", product_list_view, name="product_list")
]
