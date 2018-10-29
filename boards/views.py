from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Board, Topic, Post

from .forms  import NewTopicForm, NewPostForm


'''
def home(request):
  return render(request, 'boards/home.html')
'''

def boards(request):
  ''' displays all boards
  '''
  boards= Board.objects.all()
  return render(request, 'boards/boards.html', {'boards': boards})


def board_topics(request, board_pk):
  ''' displays all topics under a particular board
  '''
  board = get_object_or_404(Board, pk= board_pk)
  return render(request, 'boards/board_topics.html', {'board': board})  


def topic_posts(request, board_pk, topic_pk):
  ''' displays all posts under this particular topic
  '''
  topic= get_object_or_404(Topic, pk= topic_pk)
  return render(request, 'boards/topic_posts.html', {'topic': topic})


def new_topic(request, board_pk):
  ''' add a new topic
  '''
  board= get_object_or_404(Board, pk= board_pk)

  form= NewTopicForm()
  if request.method== 'POST':
    form= NewTopicForm(request.POST)
    if form.is_valid():
      #form.save()
      print(request.POST)
      return HttpResponseRedirect(reverse('boards:boards'))
  return render(request, 'boards/new_topic.html', {'form': form})


def new_post(request):
  ''' add a new topic
  '''
  form= NewPostForm()
  return render(request, 'boards/new_post.html', {'form': form})


