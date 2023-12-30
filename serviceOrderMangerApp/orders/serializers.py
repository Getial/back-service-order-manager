# Django
from django.contrib.auth import password_validation, authenticate
# from django.core.validators import RegexValidator, FileExtensionValidator

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django_filters import rest_framework as filters
from .models import Brand, Category, Reference, Client, User, Order, Evidence


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'warranty_service', 'company')


class CategorySerializer(serializers.ModelSerializer):
    type_description = serializers.ReadOnlyField(source="get_type_display")

    class Meta:
        model = Category
        fields = ('id', 'name', 'type_description')


class ReferenceFilter(filters.Filter):
    brand = filters.NumberFilter(field_name='brand', lookup_expr='exact')
    category = filters.NumberFilter(field_name='category', lookup_expr='exact')

    class Meta:
        model = Reference
        fields = {
            'brand': ['exact'],
            'category': ['exact']
        }


class ReferenceSerializer(serializers.ModelSerializer):
    brand_name = serializers.ReadOnlyField(source='brand.name')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Reference
        fields = ('id', 'brand', 'brand_name', 'category', 'category_name', 'reference',
                  'manpower', 'exploded_view')
        filterset_class = ReferenceFilter


class ClientFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='fullname', lookup_expr='icontains')

    class Meta:
        model = Client
        fields = {
            'fullname': ['icontains']
        }


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'fullname', 'genred', 'is_company', 'document', 'phone_number',
                  'second_phone_number', 'email', 'municipality', 'address')
        filterset_class = ClientFilter


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'fullname', 'occupation', 'email')


class UserLoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Primero validamos los datos
    def validate(self, data):
        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(
            email=data['email'], password=data['password'])
        print(f'user {user}')
        if not user:
            raise serializers.ValidationError(
                'Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(
            user=self.context['user'])
        return self.context['user'], token.key


class UserSignUpSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    fullname = serializers.CharField(
        min_length=4,
        max_length=30,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        min_length=4,
        max_length=30,
    )

    # phone_regex = RegexValidator(
    #     regex=r'\+?1?\d{9,15}$',
    #     message="Debes introducir un número con el siguiente formato: +999999999. El límite son de 15 dígitos."
    # )
    # phone = serializers.CharField(validators=[phone_regex], required=False)

    occupation = serializers.CharField(min_length=8, max_length=64)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)

        # image = None
        # if 'photo' in data:
        #     image = data['photo']

        # if image:
        #     if image.size > (512 * 1024):
        #         raise serializers.ValidationError(f"La imagen es demasiado grande, el peso máximo permitido es de 512KB y el tamaño enviado es de {round(image.size / 1024)}KB")

        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user


class OrderFilter(filters.FilterSet):
    service_number = filters.CharFilter(
        method='filter_by_search', lookup_expr='icontains')

    def filter_by_search(self, queryset, value):
        return queryset.filter(service_number__icontains=value) | queryset.filter(client__fullname__icontains=value)

    class Meta:
        model = Order
        fields = {
            'service_number': ['icontains'],
        }


class OrderSerializer(serializers.ModelSerializer):
    brand_name = serializers.ReadOnlyField(source='brand.name')
    category_name = serializers.ReadOnlyField(source='category.name')
    reference_name = serializers.ReadOnlyField(source='reference.reference')
    client_name = serializers.ReadOnlyField(source='client.fullname')
    client_address = serializers.ReadOnlyField(source='client.address')
    client_municipality = serializers.ReadOnlyField(
        source='client.municipality')
    client_phone_number = serializers.ReadOnlyField(
        source='client.phone_number')
    state_description = serializers.ReadOnlyField(source="get_state_display")
    # evidences = serializers.ReadOnlyField(source="evidences.image")

    class Meta:
        model = Order
        fields = ('id', 'entry_date', 'is_guarantee', 'service_number', 'brand', 'brand_name',
                  'category', 'category_name', 'reference', 'reference_name', 'serial', 'client', 'client_name', 'client_address',
                  'client_municipality', 'client_phone_number', 'reason_for_entry', 'observations', 'diagnostic', 'is_necesary_spare_parts', 'spare_parts_list',
                  'estimate_for_repair', 'payment', 'payment_for_revision',
                  'paid', 'received_by', 'checked_by', 'repared_by', 'dispatched_by', 'state', 'state_description', 'evidences')
        # filterset_class = OrderFilter


class OrderSimpleSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='client.fullname')
    state_description = serializers.ReadOnlyField(source="get_state_display")

    class Meta:
        model = Order
        fields = ('id', 'entry_date', 'service_number',
                  'client_name', 'state_description')


class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ('id', 'image', 'order')
