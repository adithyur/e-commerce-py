from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('cart/', views.cart_detail,name='cart_detail'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('increment_item/<int:item_id>/', views.increment_item, name='increment_item'),
    path('decrement_item/<int:item_id>/', views.decrement_item, name='decrement_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
]
