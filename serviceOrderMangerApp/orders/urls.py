from django.urls import path
from .views import BrandViewSet, CategoryViewSet, ReferenceViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('brands', BrandViewSet, basename='brands')
router.register('categories', CategoryViewSet, basename='categories')
router.register('referencies', ReferenceViewSet, basename='referencies')
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = router.urls