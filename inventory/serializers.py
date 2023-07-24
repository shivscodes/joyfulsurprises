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

class SuperCategorySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = SuperCategory
        fields = ['name', 'categories']

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