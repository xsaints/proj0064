from django.conf.urls import url
from . import views


app_name= 'shop'

urlpatterns= [

  url(r'^about/$', views.about, name= 'about'),

  # to list all categories
  url(r'^$', views.CategoryListView.as_view(), name= 'categories'),

  # to list all products under a category (url - shop/1, 1 is category ex. Electronics)
  url(r'^(?P<pk>\d+)/$', views.ProductListView.as_view(), name= 'products'),
  #url(r'^<int:pk>/<int:pk2>/$', views.ProductListView.as_view(), name= 'products'),  

  # to display a single product under a category
  #url(r'^(?P<category_pk>\d+)/product/(?P<product_pk>\d+)/$', views.ProductDetailView.as_view(), name= 'product'),  
  url(r'^product/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name= 'product'),  
  #url(r'^product/(?P<slug>[\w-]+)/$', views.ProductDetailView.as_view(), name= 'product'),  

  # to add a new product
  #url(r'^product/create/$', views.ProductCreateView.as_view(), name= 'product_create'),  

]