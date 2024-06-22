from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product

class ProductListView(generic.ListView):
   model = Product
   template_name ='my_products/product_list.html'
   context_object_name = 'products'


def product_detail(request, pk):
   product = get_object_or_404(Product, pk=pk)
   return render(request, 'my_products/product_detail.html',{'product':product})