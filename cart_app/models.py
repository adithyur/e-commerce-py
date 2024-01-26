from django.db import models
from productapp.models import Product

class Cart(models.Model):
    cart_id=models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['created_at']

    def __str__(self):
        return '{}' .format(self.cart_id)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)

    class Meta:
        db_table='CartItem'

    def sub_total(self):
        return self.product.price* self.quantity
    
    def __str__(self):
        return '{}' .format(self.product)

