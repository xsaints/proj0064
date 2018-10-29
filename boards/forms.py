from django import forms

from .models import Board, Topic, Post

class NewTopicForm(forms.ModelForm):
  class Meta:
    model= Topic
    fields= ['subject',]


class NewPostForm(forms.ModelForm):
  class Meta:
    model= Post
    fields= '__all__'