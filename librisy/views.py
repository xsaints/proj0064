#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Genre, Author, Book, BookInstance


def home(request):
  #return HttpResponse('<h1>mabuhay</h1>')
  return render(request, 'librisy/home.html')


def book_list(request, genre_id= None, author_id= None):
  genre = None
  genres = Genre.objects.all()
  author = None
  authors= Author.objects.all()
  books  = Book.objects.all()


  if genre_id:
    genre= get_object_or_404(Genre, id= genre_id)
    books= Book.objects.filter(genre= genre)

  if author_id:
    author= get_object_or_404(Author, id= author_id)
    books= Book.objects.filter(author= author)

  context= {'genres': genres, 'genre': genre, 'books': books,
    'author': author, 'authors': authors
  }
  return render(request, 'librisy/book_list.html', context)
