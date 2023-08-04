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
        fields = ('name', 'type')
        
        
class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ('brand', 'category', 'reference', 'manpower', 'exploded_view')
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('fullname', 'document', 'phone_number', 'second_phone_number', 'department', 'municipality', 'address')
        

class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = ('name', 'occupation', 'email', 'password')
        
        
class OrderFilter(filters.FilterSet):
    brand = filters.NumberFilter(field_name="brand_of_the_product", lookup_expr="exact")
    user = filters.NumberFilter(field_name='user', lookup_expr='exact')
    class Meta:
        model = Order
        fields = {
            'brand_of_the_product': ['exact'],
        }
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('entry_date', 'is_guarantee', 'service_number', 'brand_of_the_product',
                  'category', 'reference', 'serial', 'user', 'observations', 'diagnostic',
                  'received_by', 'estimate_for_repair', 'payment', 'payment_for_revision',
                  'paid', 'checked_and_or_repaired_by', 'state')
        filterset_class = OrderFilter
        
        
class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ('image', 'order')