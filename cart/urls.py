from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CheckoutView
from django.urls import path

router = DefaultRouter()
router.register(r'carts', CartViewSet)

urlpatterns = router.urls + [
    path('order/create', CheckoutView.as_view(), name='create-order')
]