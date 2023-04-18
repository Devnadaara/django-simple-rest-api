from django.urls import path,include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register(r'products',views.ProductViewSet,basename='products')
router.register(r'collections',views.CollectionViewSet)
router.register(r'customers',views.CustomerViewSet)

urlpatterns =[
        path('',include(router.urls))
]