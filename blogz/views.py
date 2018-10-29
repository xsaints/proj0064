from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def home(request):
  return HttpResponse('<h2>BlogZ</h2>')


