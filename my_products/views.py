from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product,Comment
from .forms import CommentForm

class ProductListView(generic.ListView):
   model = Product
   template_name ='my_products/product_list.html'
   context_object_name = 'products'


def product_detail(request, pk):
   product = get_object_or_404(Product, pk=pk)
   comments = Comment.objects.filter(active=True)
   if request.method =='POST':
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
         new_comment =comment_form.save(commit= False)
         new_comment.product = product
         new_comment.author = request.user
         new_comment.sav()
         comment_form= CommentForm()

   else:
      comment_form = CommentForm()
   return render(request, 'my_products/product_detail.html',{'product':product, 'comment_form':comment_form})


