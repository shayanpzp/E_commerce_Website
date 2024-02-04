from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImage, ProductReview, Wishlist, Address    

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()

    if request.user.is_authenticated:
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            address = None 
    
    return {
        "categories" : categories,
        "address" : address,
        "vendors" : vendors,
    }