from rest_framework import serializers
from .models import SuperCategory, Category, SubCategory, CircleCategory,MainBanner, Product

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'subcategories']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        subcategories = instance.subcategory_set.all()
        representation['subcategories'] = SubCategorySerializer(subcategories, many=True).data if subcategories else []
        return representation

class SuperCategorySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = SuperCategory
        fields = ['name','is_active','image', 'categories']
        
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        categories = instance.category_set.prefetch_related('subcategory_set')
        filtered_categories = [cat for cat in categories if cat.subcategory_set.exists()]
        representation['categories'] = CategorySerializer(filtered_categories, many=True).data
        return {'super_categories': [representation]}
    
        

class CircleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CircleCategory
        fields = ('id', 'circle_image', 'alt_text', 'circle_category_name')

class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'