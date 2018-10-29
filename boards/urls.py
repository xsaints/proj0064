from django.conf.urls import url

from boards import views


app_name= 'boards'


urlpatterns= [

  # display all boards
  url(r'^$', views.boards, name= 'boards'),

 # display all topics under this board
  url(r'^(?P<board_pk>\d+)/$', views.board_topics, name= 'board_topics'),

  # display all posts under this topic
  url(r'^(?P<board_pk>\d+)/(?P<topic_pk>\d+)/$', views.topic_posts, name= 'topic_posts'),

  # new topic
  url(r'^(?P<board_pk>\d+)/new_topic/$', views.new_topic, name= 'new_topic'),

  # new post
  url(r'new_post/$', views.new_post, name= 'new_post'),


]