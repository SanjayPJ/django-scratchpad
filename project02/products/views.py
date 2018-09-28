from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product

# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()