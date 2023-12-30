from rest_framework import viewsets, status
from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import Brand, Category, Reference, User, Client, Order, Evidence
from . serializers import BrandSerializer, CategorySerializer, ReferenceSerializer, UserSerializer, UserLoginSerializer, UserSignUpSerializer, ClientSerializer, OrderSerializer, OrderSimpleSerializer, EvidenceSerializer


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data['email']
        password = request.data["password"]
        user = authenticate(request, email=email, password=password)
        if not user:
            return JsonResponse("usuario no encontrado", safe=False,
                                status=status.HTTP_404_NOT_FOUND)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        # """User sign in."""
        # serializer = UserLoginSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user, token = serializer.save()
        # data = {
        #     'user': UserSerializer(user).data,
        #     'access_token': token
        # }
        # return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


class EvidenceViewSet(viewsets.ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-entry_date')
    serializer_class = OrderSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search = self.request.query_params.get('os', None)
    #     if search is not None:
    #         queryset = queryset.filter(service_number__icontains=search)
    #     return queryset

    @action(detail=False, methods=['get'])
    def searchorder(self, request):
        queryset = super().get_queryset()
        search = self.request.query_params.get('os', None)
        if search is not None:
            queryset = queryset.filter(service_number__icontains=search) | queryset.filter(
                client__fullname__icontains=search)
        return Response(OrderSimpleSerializer(queryset, many=True).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def lastorder(self, request):
        queryset = Order.objects.all().filter(
            is_guarantee=False).order_by('-entry_date')[:1]
        return Response(OrderSerializer(queryset, many=True).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def simpleinformation(self, request):
        queryset = Order.objects.all().exclude(state="delivered").order_by('-entry_date')
        return Response(OrderSimpleSerializer(queryset, many=True).data, status=status.HTTP_200_OK)
