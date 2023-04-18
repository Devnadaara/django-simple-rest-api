
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProductSelializer,CollectionSerializer ,CustomerSerializer
from .models import Product,Collection,Customer
# Create your views here.



class CustomerViewSet(CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


    @action(detail=False,methods= ['GET','PUT'])
    def me(self,request):
        (customer,created) =Customer.objects.get_or_create( user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method  == 'PUT':
           serializer = CustomerSerializer(customer,data=request.data)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response(serializer.data)


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
  









           

