from rest_framework import viewsets, status
from django.contrib.auth import password_validation, authenticate
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import Brand, Category, Reference, Collaborator, Client, Order, Evidence
from . serializers import BrandSerializer, CategorySerializer, ReferenceSerializer, CollaboratorSerializer, CollaboratorLoginSerializer, ClientSerializer, OrderSerializer, EvidenceSerializer


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
        category = self.request.query_params.get('category')
        if brand and category:
            queryset = queryset.filter(brand=brand).filter(category=category)

        return queryset


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(fullname__icontains=name)
        return queryset


class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data['email']
        password = request.data["password"]
        print(email)
        print(password)
        user = authenticate(email=email, password=password)
        return Response(user, status=status.HTTP_200_OK)
        """Collaborator sign in."""
        # serializer = CollaboratorLoginSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user, token = serializer.save()
        # data = {
        #     'user': CollaboratorSerializer(user).data,
        #     'access_token': token
        # }
        # return Response(data, status=status.HTTP_201_CREATED)


class EvidenceViewSet(viewsets.ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-entry_date')
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        last = self.request.query_params.get('last', None)
        if last is not None:
            queryset = queryset.filter(is_guarantee=False)
        return queryset
