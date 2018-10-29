from django.conf.urls import url

from . import views


app_name= 'cbv001'

urlpatterns= [
  #url('^$', views.home, name= 'cbv001_home'),
  #url('^$', views.cbv_home.as_view(), name= 'cbv001_home'),
  url('^$', views.cbv_home2.as_view(), name= 'cbv001_home'),  

]