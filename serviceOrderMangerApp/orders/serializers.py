from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Brand, Category, Reference, User, Collaborator, Order, Evidence


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'warranty_service', 'company')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'type')


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


class UserFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='fullname', lookup_expr='icontains')

    class Meta:
        model = User
        fields = {
            'fullname': ['icontains']
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'fullname', 'document', 'phone_number',
                  'second_phone_number', 'email', 'municipality', 'address')
        filterset_class = UserFilter


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = ('id', 'name', 'occupation', 'email', 'password')


class OrderFilter(filters.FilterSet):
    is_guarantee = filters.NumberFilter(
        field_name='is_guarantee', lookup_expr='exact')

    class Meta:
        model = Order
        fields = {
            'is_guarantee': ['exact'],
        }


class OrderSerializer(serializers.ModelSerializer):
    name_brand = serializers.ReadOnlyField(source='brand_id.name')
    category_name = serializers.ReadOnlyField(source='category.name')
    user_name = serializers.ReadOnlyField(source='user.fullname')
    state_description = serializers.ReadOnlyField(source="get_state_display")

    class Meta:
        model = Order
        fields = ('id', 'entry_date', 'is_guarantee', 'service_number', 'brand_id', 'name_brand',
                  'category', 'category_name', 'reference', 'serial', 'user', 'user_name', 'reason_for_entry', 'observations', 'diagnostic',
                  'received_by', 'estimate_for_repair', 'payment', 'payment_for_revision',
                  'paid', 'checked_by', 'repared_by', 'dispatched_by', 'state', 'state_description')
        filterset_class = OrderFilter


class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ('image', 'order')
