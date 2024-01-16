from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from .views import BrandViewSet, CategoryViewSet, ReferenceViewSet, ClientViewSet, UserViewSet, OrderViewSet, EvidenceViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings # new
from  django.conf.urls.static import static #new

router = DefaultRouter()
router.register('brands', BrandViewSet, basename='brands')
router.register('categories', CategoryViewSet, basename='categories')
router.register('referencies', ReferenceViewSet, basename='referencies')
router.register('clients', ClientViewSet, basename='clients')
router.register('users', UserViewSet, basename='users')
router.register('orders', OrderViewSet, basename='orders')
router.register('evidences', EvidenceViewSet, basename='evidences')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title="Order API")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)