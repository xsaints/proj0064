from django.conf.urls import url
from . import views



app_name= 'cart'

urlpatterns= [
  url('^$', views.cart_home, name= 'home'),

]