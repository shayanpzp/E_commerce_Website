from django.urls import path, include
from core.views import index, category_list_view, product_list_view, category_product_list__view, vendor_list_view,vendor_detail_view,product_detail_view,tag_list,ajax_add_review,search_view,filter_product,add_to_cart,cart_view,delete_item_from_cart,update_from_cart,checkout_view,customer_dashboard,order_detail

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("category/", category_list_view, name="category_list"),
    path("products/", product_list_view, name="product_list"),
    path("product/<pid>/", product_detail_view, name="product_detail"),
    path("category/<cid>/", category_product_list__view, name="category_product_list"),
    path("vendors/", vendor_list_view, name="vendor_list"),
    path("vendor/<vid>/", vendor_detail_view, name="vendor_detail"),
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),
    path("ajax_add_review/<int:pid>", ajax_add_review, name="ajax_add_review"),
    path("search/", search_view, name="search"),
    path("filter-products/", filter_product, name="filter-product"),
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path("cart/",cart_view, name="cart"),
    path("delete-from-cart/",delete_item_from_cart, name="delete-from-cart"),
    path("update-cart/",update_from_cart, name="update-cart"),
    path("checkout/",checkout_view, name="checkout"),
    path("paypal/", include('paypal.standard.ipn.urls')),
    path("dashboard/",customer_dashboard, name="dashboard"),
    path("dashboard/order/<int:id>/",order_detail, name="order-detail"),
    
]
