from rest_framework import serializers
from .models import Product,Collection





class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Collection
        fields = ['id','title','products_count']

class ProductSelializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','inventory','collection','unit_price']

    