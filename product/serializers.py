from rest_framework import serializers
from .models import Product , Brand , ProductImages
from django.db.models.aggregates import Avg



class ProductImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImages
        fields = ['image']



class ProductListSerializer(serializers.ModelSerializer):
   # brand = BrandSerializer()
   brand = serializers.StringRelatedField()
   price_with_tax = serializers.SerializerMethodField()
   avg_rate= serializers.SerializerMethodField()
   #price_with_tax = serializers.SerializerMethodField(method_name='myfunc')

   class Meta:
        model = Product
        fields = '__all__'

   def get_price_with_tax(self,product):
       return product.price*1.1    

   def get_avg_rate(self,product):
        avg = product.product_review.aggregate(rate_Avg=Avg('rate'))   
        avg_rate = avg['rate_Avg'] 
        if avg_rate :
            avg_rate = round(avg_rate,)
        else:
            avg_rate = 0
        return avg_rate        


   #def myfunc(self,product):
       #return product.price*1.1

class ProductDetailSerializer(serializers.ModelSerializer):
   brand = serializers.StringRelatedField()
   image = ProductImagesSerializer(source='product_image',many=True)

   class Meta:
        model = Product
        fields = '__all__'       

class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'         


class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(source='product_brand',many=True)

    class Meta:
        model = Brand
        fields = '__all__'       