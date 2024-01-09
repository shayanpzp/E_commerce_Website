from rest_framework import serializers
from rest_framework.fields import empty
from . import models



class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model =models.Seller
        fields = ['id','user', 'address']
        
    def __init__(self, *args, **kwargs):
        super(SellerSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1
        
        
class SellerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =models.Seller
        fields = ['id','user', 'address']
        
        
    def __init__(self, *args, **kwargs):
        super(SellerDetailSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1