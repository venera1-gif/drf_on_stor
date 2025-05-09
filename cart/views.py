from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import OrderSerializer
from rest_framework.decorators import action
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from django.shortcuts import get_list_or_404

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all() 
    serializer_class = CartSerializer

    @action(detail=True, methods=['post'])
    def add_item(self, request): 
        cart = self.get_object()
        serializer = CartItemSerializer(data=reguest.data)
        if serializer.is_valid():
            product = serializer.validated_data['product']
            quantity = serializer.validated_data['quantity'] 
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.guantity += guantity 
            cart_item.save()
            return Response(CartItemSerializer(cart_item).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REGUEST)
    
    @action(detail=True, methods=['post'])
    def remove_item(self, reguest,):
        cart = self.get_object()
        product_id = reguest.data.get('product_id')
        item = get_list_or_404(CartItem, cart=cart, product_id=product_id)
        item.delete()
        return Response({'status': 'item removed'}) 
    
class CheckoutView(APIView):
    def post(self,reguest):
        session_key = reguest.session.session_key
        if not session_key:
           return Response({"error": "No session"}, status=400)
        
        cart = Cart.objects.filter(session_key=session_key).first()
        if not cart or cart.items.count()==0:
            return Response({"error": "Cart is empty"}, status=400)
        
        full_name = reguest.data.get('full_name')
        address =reguest.data.get('address')
        phone = reguest.data.get('phone')

        order = Order.objects.create(
            session_key=session_key,
            full_name=full_name,
            address=address,
            phone=phone
        )

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product_name=item.product.title,
                price=item.product.price,
                quantity=item.quantity
            )

        cart.items.all().delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


