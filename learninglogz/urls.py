from django.conf.urls import url

from learninglogz import views

app_name= 'learninglogz'


urlpatterns= [
  url(r'^$', views.home, name= 'home'),


]

