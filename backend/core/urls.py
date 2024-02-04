from django.urls import path
from core.views import index, category_list_view, product_list_view, category_product_list__view, vendor_list_view,vendor_detail_view,product_detail_view,tag_list,ajax_add_review,search_view,filter_product

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
    path("filter-products/", filter_product, name="filter-product")
    
]
