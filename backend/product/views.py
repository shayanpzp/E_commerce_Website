from django.shortcuts import render
from audioop import avg
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProductReviewForm
from .models import Product, Category, ProductReview


class ProductListView(TemplateView):
    template_name = "core/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(product_status="published")
        return context
    
    
class ProductDetailView(TemplateView):
    template_name = "core/product_detail.html"

    def get_context_data(self, **kwargs):
        product = get_object_or_404(Product, pid=self.kwargs['pid'])
        products = Product.objects.filter(category=product.category).exclude(pid=self.kwargs['pid'])
        reviews = ProductReview.objects.filter(product=product).order_by("-date")
        average_rating = ProductReview.objects.filter(product=product).aggregate(rating=avg('rating'))
        product_image = product.product_images.all()
        review_form = ProductReviewForm()
        make_review = True
        if self.request.user.is_authenticated:
            user_review_count = ProductReview.objects.filter(user=self.request.user, product=product).count()
            if user_review_count > 0:
                make_review = False
        context = {
            "product": product,
            "make_review": make_review,
            "review_form": review_form,
            "product_image": product_image,
            "average_rating": average_rating,
            "reviews": reviews,
            "products": products,
        }
        return context

class FilterProductView(View):
    def get(self, request):
        categories = request.GET.getlist("category[]")
        vendors = request.GET.getlist("vendor[]")
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        products = Product.objects.filter(product_status="published").order_by("-id").distinct()
        products = products.filter(price__gte=min_price, price__lte=max_price)
        if len(categories) > 0:
            products = products.filter(category__id__in=categories).distinct()
        if len(vendors) > 0:
            products = products.filter(vendor__id__in=vendors).distinct()

        product_data = []
        for product in products:
            product_data.append({
                'id': product.id,
                'title': product.title,
                'price': product.price,
            })

        return JsonResponse({"data": product_data})
    
    
class AddReviewView(View):
    def post(self, request, pid):
        product = get_object_or_404(Product, pk=pid)
        user = request.user
        review = ProductReview.objects.create(
            user=user,
            product=product,
            review=request.POST['review'],
            rating=request.POST['rating'],
        )
        average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=avg('rating'))
        return JsonResponse({
            'bool': True,
            'user': user.username,
            'review': request.POST['review'],
            'rating': request.POST['rating'],
            'average_reviews': average_reviews
        })