from rest_framework import serializers
from .models import Product,Collection,Customer





class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Customer
        fields = ['id','phone','birth_date','user_id']



class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Collection
        fields = ['id','title','products_count']

class ProductSelializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','inventory','collection','unit_price']

    