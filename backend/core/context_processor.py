from vendor.models import Vendor
from product.models import Product
from category.models import Category
from core.models import CartOrder, CartOrderItems, Wishlist, Address    
from django.db.models import Min,Max



def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    
    min_max_price = Product.objects.aggregate(Min("price"), Max("price"))
    address = None 
    if request.user.is_authenticated:
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            pass
    
    return {
        "categories" : categories,
        "address" : address,
        "vendors" : vendors,
        "min_max_price" : min_max_price,
    }