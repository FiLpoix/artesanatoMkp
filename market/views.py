from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User, Category, Product, Artisan, Customer
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, ArtisanSerializer, CustomerSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArtisanViewSet(viewsets.ModelViewSet):
    queryset = Artisan.objects.all()
    serializer_class = ArtisanSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer