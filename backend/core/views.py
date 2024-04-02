from audioop import avg
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from product.models import Product
from customer.models import Profile
from .models import  Tags, CartOrder, CartOrderItems, Address

class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(product_status="published", featured=True)
        return context



class TagListView(TemplateView):
    template_name = "core/tag.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(product_status="published").order_by("-id")
        tag = None
        if 'tag_slug' in self.kwargs:
            tag = get_object_or_404(Tags, slug=self.kwargs['tag_slug'])
            products = products.filter(tags__in=[tag])
        context["products"] = products
        context["tag"] = tag
        return context



class SearchView(TemplateView):
    template_name = "core/search.html"

    def get_context_data(self, **kwargs):
        query = self.request.GET.get("q")
        products = Product.objects.filter(title__icontains=query).order_by("-date")
        context = {
            "products": products,
            "query": query,
        }
        return context




class AddToCartView(View):
    def get(self, request):
        cart_product = {}
        cart_product[str(request.GET['id'])] = {
            'title': request.GET['title'],
            'qty': request.GET['qty'],
            'price': request.GET['price'],
            'image': request.GET['image'],
            'pid': request.GET['pid'],
        }
        if 'cart_data_obj' in request.session:
            if str(request.GET['id']) in request.session['cart_data_obj']:
                cart_data = request.session['cart_data_obj']
                cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
                cart_data.update(cart_data)
                request.session['cart_data_obj'] = cart_data
            else:
                cart_data = request.session['cart_data_obj']
                cart_data.update(cart_product)
                request.session['cart_data_obj'] = cart_data
        else:
            request.session['cart_data_obj'] = cart_product
        cart_total_amount = 0
        if 'cart_data_obj' in request.session:
            for product_id, item in request.session['cart_data_obj'].items():
                qty = int(item.get('qty', 0))
                price_str = item.get('price', '')
                if price_str and price_str.replace('.', '', 1).isdigit():
                    price = float(price_str)
                    cart_total_amount += qty * price
        context = {
            "cart_data": request.session['cart_data_obj'],
            'totalcartitems': len(request.session['cart_data_obj']),
            'cart_total_amount': cart_total_amount
        }
        return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})

class CartView(TemplateView):
    template_name = "core/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_total_amount = 0
        if 'cart_data_obj' in self.request.session:
            for product_id, item in self.request.session['cart_data_obj'].items():
                qty = int(item.get('qty', 0))
                price_str = item.get('price', '')
                if price_str and price_str.replace('.', '', 1).isdigit():
                    price = float(price_str)
                    cart_total_amount += qty * price
            context["cart_data"] = self.request.session['cart_data_obj']
            context['totalcartitems'] = len(self.request.session['cart_data_obj'])
            context['cart_total_amount'] = cart_total_amount
        else:
            messages.warning(self.request, "سبد خرید شما خالی می باشد")
            return redirect("core:index")
        return context

class DeleteItemFromCartView(View):
    def get(self, request):
        product_id = str(request.GET['id'])
        if 'cart_data_obj' in request.session:
            if product_id in request.session['cart_data_obj']:
                cart_data = request.session['cart_data_obj']
                del request.session['cart_data_obj'][product_id]
                request.session['cart_data_obj'] = cart_data
        cart_total_amount = 0
        if 'cart_data_obj' in request.session:
            for product_id, item in request.session['cart_data_obj'].items():
                qty = int(item.get('qty', 0))
                price_str = item.get('price', '')
                if price_str and price_str.replace('.', '', 1).isdigit():
                    price = float(price_str)
                    cart_total_amount += qty * price
        context = {
            "cart_data": request.session['cart_data_obj'],
            'totalcartitems': len(request.session['cart_data_obj']),
            'cart_total_amount': cart_total_amount
        }
        return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})

class UpdateFromCartView(View):
    def get(self, request):
        product_id = str(request.GET['id'])
        product_qty = request.GET['qty']
        if 'cart_data_obj' in request.session:
            if product_id in request.session['cart_data_obj']:
                cart_data = request.session['cart_data_obj']
                cart_data[str(request.GET['id'])]['qty'] = product_qty
                request.session['cart_data_obj'] = cart_data
        cart_total_amount = 0
        if 'cart_data_obj' in request.session:
            for product_id, item in request.session['cart_data_obj'].items():
                qty = int(item.get('qty', 0))
                price_str = item.get('price', '')
                if price_str and price_str.replace('.', '', 1).isdigit():
                    price = float(price_str)
                    cart_total_amount += qty * price
        context = {
            "cart_data": request.session['cart_data_obj'],
            'totalcartitems': len(request.session['cart_data_obj']),
            'cart_total_amount': cart_total_amount
        }
        return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})

class CheckoutView(TemplateView):
    template_name = "core/checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_total_amount = 0
        if 'cart_data_obj' in self.request.session:
            for product_id, item in self.request.session['cart_data_obj'].items():
                qty = int(item.get('qty', 0))
                price_str = item.get('price', '')
                if price_str and price_str.replace('.', '', 1).isdigit():
                    price = float(price_str)
                    cart_total_amount += qty * price
            context["cart_data"] = self.request.session['cart_data_obj']
            context['totalcartitems'] = len(self.request.session['cart_data_obj'])
            context['cart_total_amount'] = cart_total_amount
        return context
class CustomerDashboardView(TemplateView):
    template_name = "core/dashboard.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = CartOrder.objects.filter(user=self.request.user).order_by("-id")
        address = Address.objects.filter(user=self.request.user)
        user_profile = Profile.objects.get(user=self.request.user)
        context["user_profile"] = user_profile
        context["address"] = address
        context["orders"] = orders
        return context

class OrderDetailView(TemplateView):
    template_name = "core/order_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = CartOrder.objects.get(user=self.request.user, id=self.kwargs['id'])
        order_items = CartOrderItems.objects.filter(order=order)
        context["order_items"] = order_items
        return context

class MakeAddressDefaultView(View):
    def get(self, request):
        id = request.GET['id']
        Address.objects.update(status=False)
        Address.objects.filter(id=id).update(status=True)
        return JsonResponse({"boolean": True})


class AboutView(TemplateView):
    template_name = "core/about_us.html"
    
    
class ContactView(TemplateView):
    template_name = "core/contact_us.html"
