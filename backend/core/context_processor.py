from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImage, ProductReview, Wishlist, Address    

def default(request):
    categories = Category.objects.all()
    address = None 

    if request.user.is_authenticated:
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            pass
    
    return {
        "categories" : categories,
        "address" : address,
    }