from django.urls import path, include
from .views import (
     ProductListView, ProductDetailView, 
    AddReviewView, FilterProductView,
)

app_name = "product"

urlpatterns = [
    
    path("products/", ProductListView.as_view(), name="product_list"),
    path("product/<pid>/", ProductDetailView.as_view(), name="product_detail"),
    path("ajax_add_review/<int:pid>", AddReviewView.as_view(), name="ajax_add_review"),
    path("filter-products/", FilterProductView.as_view(), name="filter-product"),
]
