from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSelializer,CollectionSerializer 
from .models import Product,Collection
# Create your views here.



class ProductViewSet(ModelViewSet):
     serializer_class = ProductSelializer

     def get_queryset(self):
        queryset = Product.objects.all()
        collection_id =self.request.query_params.get('collection_id')
        if collection_id is not None:
            queryset = Product.objects.filter(collection_id =collection_id)
        return queryset

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
             products_count= Count('products')
        ).all()
    serializer_class = CollectionSerializer
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id = kwargs['pk']).count() > 0:
            return Response({'detail':"collection can't be deleted because it associated with a product"})
        return super().destroy(request, *args, **kwargs)
  









           

