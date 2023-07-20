from rest_framework import serializers
from .models import Category, Inventory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Inventory
        fields = '__all__'
