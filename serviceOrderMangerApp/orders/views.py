from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import Brand, Category, Reference, Collaborator, User, Order, Evidence
from . serializers import BrandSerializer, CategorySerializer, ReferenceSerializer, CollaboratorSerializer, UserSerializer, OrderSerializer, EvidenceSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # filtrado por marca
        brand = self.request.query_params.get('brand')
        if brand:
            queryset = queryset.filter(brand=brand)

        # filtrado por usuario
        user = self.request.query_params.get('user')
        if user:
            queryset = queryset.filter(user=user)

        return queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer


class EvidenceViewSet(viewsets.ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
