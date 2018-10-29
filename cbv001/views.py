from django.shortcuts import render
from django.views.generic import (View, TemplateView)
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'cbv001/home.html')


class cbv_home(View):
  def get(self, request):
    return HttpResponse("cbv is cool")

class cbv_home2(TemplateView):    
    template_name = 'cbv001/home.html'

    def get_context_data(self, *args, **kwargs):
      context= super().get_context_data(*args, **kwargs)
      context['x']= 'whatever'
      context['y']= 'heller'
      return context
