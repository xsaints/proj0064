from django.conf.urls import url

from librisy import views


app_name= 'librisy'


urlpatterns= [

  url(r'^$', views.book_list, name= 'home'),

  url(r'^genres/$', views.book_list, name= 'all_genres'),
  url(r'^genres/(?P<genre_id>[-\w]+)$', views.book_list, name= 'books_by_genre'),  

  url(r'^authors/$', views.book_list, name= 'all_authors'),    
  url(r'^authors/(?P<author_id>[-\w]+)$', views.book_list, name= 'books_by_author'),    

]
