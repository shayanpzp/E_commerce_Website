from rest_framework import serializers
from . import models



class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model =models.Seller
        fields = ['user', 'address']