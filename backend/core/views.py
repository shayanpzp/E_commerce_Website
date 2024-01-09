# from django.shortcuts import render
from rest_framework import generics,permissions
from . import serializers
from . import models





class SellerList(generics.ListCreateAPIView): 
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    
class SellerDetails(generics.RetrieveUpdateDestroyAPIView): 
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
    # permission_classes = [permissions.IsAuthenticated]
    