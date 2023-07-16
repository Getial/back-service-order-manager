from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Brand, Category, Reference, Collaborator, User, Order, Evidence
from. serializers import BrandSerializer, CategorySerializer, ReferenceSerializer, CollaboratorSerializer, UserSerializer, OrderSerializer, EvidenceSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    
    @action(detail=False)
    def by_brand(self, request):
        brand = self.request.query_params.get('brand', None)
        referencies = Reference.objects.filter(brand=brand)
        serilizer = ReferenceSerializer(referencies, many=True)
        return Response(serilizer.data)
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    