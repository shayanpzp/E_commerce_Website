from django.shortcuts import render, get_object_or_404
from . import serializers
from . import models
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImage, ProductReview, Wishlist, Address    
from django.db.models import Count


def index(request): 
    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published", featured=True)
    
    context = {
        "products" : products
    }
    return render(request, "core/index.html", context)



def product_list_view(request):
    products = Product.objects.filter(product_status="published")
    
    context = {
        "products" : products
    }
    return render(request, "core/product_list.html", context)




def category_list_view(request): 
    # categories = Category.objects.all().annotate(product_count=Count("product"))
    categories = Category.objects.all()
    
    context = {
        "categories" : categories
    }
    return render(request, "core/category_list.html", context)




def category_product_list__view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)
    
    
    context = {
        "category" : category,
        "products" : products,
    }
    return render(request, "core/category_product_list.html", context)




def vendor_list_view(request):
    vendors = Vendor.objects.all()    
    
    context = {
        "vendors" : vendors,
        
    }
    return render(request, "core/vendor_list.html", context)




def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)  
    products = Product.objects.filter(product_status="published", vendor=vendor)
      
    
    context = {
        "vendor" : vendor,
        "products" : products,
        
    }
    return render(request, "core/vendor_detail.html", context)

    
    
def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)      
    product_image = product.product_images.all()
    
    context = {
        "product" : product,
        "product_image" : product_image,
        
    }
    return render(request, "core/product_detail.html", context)
    