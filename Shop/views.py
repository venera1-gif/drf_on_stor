from rest_framework import viewsets, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')  # ✅ Правильное название
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # ✅ Правильное название
    serializer_class = CategorySerializer






