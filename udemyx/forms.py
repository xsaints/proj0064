from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
  class Meta:
    model= Course
    fields= ['title', 'author', 'description']

    widgets = {
      'title': forms.TextInput(attrs={'size':80}),
      'description':forms.Textarea(attrs={'cols': 80, 'class':'editable'}),
    }