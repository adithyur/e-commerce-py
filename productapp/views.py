from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product

def index(request):
    return HttpResponse("Welcome to New2U")

def home(request, c_slug=None):
    category = None
    products = None
    if c_slug:
        category = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=category, available=True)
    else:
        products = Product.objects.filter(available=True)
    
    context = {
        'category': category,
        'products': products,
    }
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category.html', context)

def allproducts(request, c_slug=None):
    category = None
    products = None
    if c_slug:
        category = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=category, available=True)
    else:
        products = Product.objects.filter(available=True)
    
    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'category.html', context)

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    
    context = {
        'product': product,
    }

    return render(request, 'product_details.html', context)

