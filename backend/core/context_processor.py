from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImage, ProductReview, Wishlist, Address    


def default(request):
    categories = Category.objects.all()
    
    return {
        "categories" : categories,  
    }