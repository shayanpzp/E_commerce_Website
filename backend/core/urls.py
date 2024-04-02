from django.urls import path, include
from vendor.views import VendorDetailView, VendorListView
from product.views import AddReviewView, FilterProductView, ProductDetailView, ProductListView

from category.views import CategoryListView, CategoryProductListView
from .views import (
    IndexView, 
    TagListView, 
    SearchView, AddToCartView, CartView, 
    DeleteItemFromCartView, UpdateFromCartView, CheckoutView, 
    CustomerDashboardView, OrderDetailView, MakeAddressDefaultView,AboutView
)

app_name = "core"

urlpatterns = [
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/<cid>/", CategoryProductListView.as_view(), name="category_product_list"),
    path("", IndexView.as_view(), name="index"),
    path("vendors/", VendorListView.as_view(), name="vendor_list"),
    path("vendor/<vid>/", VendorDetailView.as_view(), name="vendor_detail"),
    path("search/", SearchView.as_view(), name="search"),
    path("add-to-cart/", AddToCartView.as_view(), name="add-to-cart"),
    path("cart/", CartView.as_view(), name="cart"),
    path("delete-from-cart/", DeleteItemFromCartView.as_view(), name="delete-from-cart"),
    path("update-cart/", UpdateFromCartView.as_view(), name="update-cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("paypal/", include('paypal.standard.ipn.urls')),
    path("dashboard/", CustomerDashboardView.as_view(), name="dashboard"),
    path("dashboard/order/<int:id>/", OrderDetailView.as_view(), name="order-detail"),
    path("make-default-address/", MakeAddressDefaultView.as_view(), name="make-address-default"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("product/<pid>/", ProductDetailView.as_view(), name="product_detail"),
    path("ajax_add_review/<int:pid>", AddReviewView.as_view(), name="ajax_add_review"),
    path("filter-products/", FilterProductView.as_view(), name="filter-product"),
    path("about/", AboutView.as_view(), name="about-us"),
]
