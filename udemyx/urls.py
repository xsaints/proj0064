from django.conf.urls import url
from django.urls import path

from udemyx import views


app_name= 'udemyx'



urlpatterns= [
  # display courses or courses by category
  url(r'^$', views.course_list, name= 'courses'),
  url(r'^(?P<category_slug>[-\w]+)/$', views.course_list, name= 'courses_by_category'),  

  # enter a new course
  url(r'^(?P<category_id>\d+)/new_course/$', views.new_course, name= 'new_course'),      

  # show all categories
  url(r'^$', views.categories, name= 'categories'),

  # show all courses under a category
  #url(r'^(?P<category_id>\d+)/$', views.courses, name= 'courses'),  

  # show details of a course
  url(r'^(?P<course_id>\d+)/(?P<slug>[-\w]+)/$', views.course_detail, name= 'course_detail'),      


  # edit a course
  url(r'^(?P<course_id>\d+)/edit_course/$', views.edit_course, name= 'edit_course'),      


]