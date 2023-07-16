from rest_framework import serializers
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
    # brand = BrandSerializer(read_only=True)
    # category = CategorySerializer(read_only=True)
    
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
        

class OrderSerializer(serializers.ModelSerializer):
    # brand_of_the_product = BrandSerializer(read_only=True)
    # category = CategorySerializer(read_only=True)
    # reference = ReferenceSerializer(read_only=True)
    # user = UserSerializer(read_only=True)
    # received_by = CollaboratorSerializer(read_only=True)
    # checked_and_or_repaired_by = CollaboratorSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = ('entry_date', 'is_guarantee', 'service_number', 'brand_of_the_product',
                  'category', 'reference', 'serial', 'user', 'observations', 'diagnostic',
                  'received_by', 'estimate_for_repair', 'payment', 'payment_for_revision',
                  'paid', 'checked_and_or_repaired_by', 'state')
        
        
class EvidenceSerializer(serializers.ModelSerializer):
    # order = OrderSerializer(read_only=True)
    
    class Meta:
        model = Evidence
        fields = ('image', 'order')