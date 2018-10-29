from django.conf.urls import url

from blogz import views

app_name= 'blogz'


urlpatterns= [

  url(r'^$', views.home, name= 'home'),


]