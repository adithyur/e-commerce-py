from django.urls import path
from .views import home, allproducts, product_detail

app_name = 'productapp'
urlpatterns = [
    path('allproducts/', allproducts, name='allproducts'),
    path('<slug:c_slug>/', allproducts, name='products_by_category'),
    path('product/<slug:product_slug>/', product_detail, name='product_detail'),
]
