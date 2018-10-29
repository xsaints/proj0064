from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from django.views.generic import (ListView, DetailView, CreateView)

from . import models


def about(request):
  print(request.session.get('first_name', 'unknown'))  
  return HttpResponse('about')

class CategoryListView(ListView):
  model= models.Category
  context_object_name= 'categories'

  def get_context_data(self, *args, **kwargs):
    context= super().get_context_data(*args, **kwargs)
    #print(context)
    return context

  

class ProductListView(DetailView):
  model= models.Category
  context_object_name= 'category'
  template_name= 'shop/product_list.html'



class xProductDetailView(ListView):
  #model= models.Product
  context_object_name= 'productss'
  #queryset= models.Product.objects.get(pk= 6)
  template_name= 'shop/product_detail.html'

  '''
  def get_queryset(self):
    self.category= get_object_or_404(models.Category, pk= self.kwargs['category_pk'])
    self.product= get_object_or_404(models.Product, pk= self.kwargs['product_pk'])
    print(type(self.category))
    print(type(int(self.product.pk)))
    print(self.kwargs['category_pk'])
    print(type(self.kwargs['product_pk']))
    return models.Product.objects.filter(pk= int(self.product.pk))
    #return None
  '''

class ProductDetailView(DetailView):
  model= models.Product
  context_object_name= 'productss'
  #queryset= models.Product.objects.all()
  template_name= 'shop/product_detail.html'
  
  
  def get_context_data(self, **kwargs):
    context= super(ProductDetailView, self).get_context_data(**kwargs)
    #q= context['product']
    #category_pk= kwargs.get('category_pk', None) 
    product_pk= kwargs.get('product_pk', None)
    #print(category_pk)
    print(product_pk)
    if product_pk:
      models.Product.objects.filter(pk= 1)
    return context
    #return None
  

class ProductCreateView(CreateView):  
    model= models.Product
    fields= ('category', 'name', 'description', 'price', 'image')