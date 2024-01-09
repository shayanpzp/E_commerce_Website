# from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models





class SellerList(generics.ListAPIView): 
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
    