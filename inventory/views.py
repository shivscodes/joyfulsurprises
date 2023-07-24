from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import SuperCategory, Category, SubCategory,CircleCategory, MainBanner, Product
from .serializers import SuperCategorySerializer, CategorySerializer, SubCategorySerializer, CircleCategorySerializer, MainBannerSerializer, ProductSerializer

# Views for SuperCategory model
class SuperCategoryListCreateView(ListCreateAPIView):
    queryset = SuperCategory.objects.all()
    serializer_class = SuperCategorySerializer

class SuperCategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SuperCategory.objects.all()
    serializer_class = SuperCategorySerializer

# Views for Category model
class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Views for Subcategory model
class SubCategoryListCreateView(ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubCategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CircleCategoryListCreateView(ListCreateAPIView):
    queryset = CircleCategory.objects.all()
    serializer_class = CircleCategorySerializer

class CircleCategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CircleCategory.objects.all()
    serializer_class = CircleCategorySerializer

class MainBannerListCreateView(ListCreateAPIView):
    queryset = MainBanner.objects.all()
    serializer_class = MainBannerSerializer

class MainBannerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = MainBanner.objects.all()
    serializer_class = MainBannerSerializer


# Views for Product model
class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
