from django.shortcuts import render
from audioop import avg
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from product.models import Product
from .models import Category


class CategoryListView(TemplateView):
    template_name = "core/category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryProductListView(TemplateView):
    template_name = "core/category_product_list.html"

    def get_context_data(self, **kwargs):
        category = get_object_or_404(Category, cid=self.kwargs['cid'])
        products = Product.objects.filter(product_status="published", category=category)
        context = {
            "category": category,
            "products": products,
        }
        return context