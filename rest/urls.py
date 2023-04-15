from django.urls import path,include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register(r'products',views.ProductViewSet,basename='products')
router.register(r'collections',views.CollectionViewSet)

urlpatterns =[
        path('',include(router.urls))
]