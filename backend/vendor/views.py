from audioop import avg
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from product.models import Product
from customer.models import Profile
from .models import Vendor



class VendorListView(TemplateView):
    template_name = "core/vendor_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vendors'] = Vendor.objects.all()
        return context

class VendorDetailView(TemplateView):
    template_name = "core/vendor_detail.html"

    def get_context_data(self, **kwargs):
        vendor = get_object_or_404(Vendor, vid=self.kwargs['vid'])
        products = Product.objects.filter(product_status="published", vendor=vendor)
        context = {
            "vendor": vendor,
            "products": products,
        }
        return context