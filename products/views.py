from django.shortcuts import render
from django.views.generic import ListView

from .models import Prouduct

class ProductListView(ListView):
    model = Prouduct
    template_name = 'products/product_list.html'
    context_object_name = 'products'

