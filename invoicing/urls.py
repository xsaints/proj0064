from django.conf.urls import url

from . import views

app_name= 'invoicing'


urlpatterns= [
  url(r'^$', views.home, name= 'home'),
  url(r'^add/$', views.add_invoice, name= 'add_invoice'),

  url(r'^employees/$', views.show_employees, name= 'show_employees'),  
  url(r'^employee/(?P<employee_id>\d+)/$', views.show_employee, name= 'show_employee'),    

  url(r'^employee/add/$', views.add_employee, name= 'add_employee'),  

]