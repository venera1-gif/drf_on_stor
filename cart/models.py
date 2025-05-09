from django.db import models
from Shop.models import Product

class Cart(models.Model):
    session_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=40)

    def __str__(self):
        return f"Cart{self.id} - Session {self.session_key}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    guantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.guantity} x {self.product.title}"
    
class Order(models.Model):
    session_key = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Order {self.id} - {self.full_name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    guantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.guantity} x {self.product_name} @ {self.price}" 
    



    

