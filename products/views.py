from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Prouduct

class ProductListView(ListView):
    model = Prouduct
    template_name = 'products/product_list.html'
    context_object_name = 'products'


def product_detail_view(request, pk):
    product = get_object_or_404(Prouduct, pk=pk)
    return render(request, 'products/product_detail.html',{'product':product})
