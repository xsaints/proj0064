#from django.http import HttpResponse
from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre


def home(request):
  #return HttpResponse('<h1>Hello library</h1>')
  return render(request, 'library/home.html', {})


def index(request):
  print(request.session)
  request.session['abc']= 'xyz'
  #request.session['abc']['wheels']= 'alloy'
  #request.session.modified= True

  num_visits= request.session.get('num_visits', 0)
  request.session['num_visits']= num_visits + 1


  num_books= Book.objects.all().count()
  num_instances= BookInstance.objects.all().count()

  num_instances_available= BookInstance.objects.filter(status__exact= 'a').count()

  num_authors= Author.objects.count()

  #abc1 = request.session.get(['abc']['wheels'])
  context= {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,        
    'abc': request.session.get('abc'),
    #'def': abc1
    'num_visits': num_visits,
  }
  return render(request, 'library/index.html', context= context)