import django_filters
from .models import Product, Category

class ProductFilter(django_filters.FilterSet):
    # Убедись, что поля существуют в модели Product
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    in_stock = django_filters.BooleanFilter(field_name="in_stock")
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'in_stock', 'price_min', 'price_max']


