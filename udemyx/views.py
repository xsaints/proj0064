from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse


from .models import Category, Course
from .forms  import CourseForm


def new_course(request, category_id):
  #return HttpResponse('<h2>Welcome</h2>')
  category= get_object_or_404(Category, id= category_id)  
  if request.method != "POST":
    form= CourseForm()
  else:
    form= CourseForm(request.POST)
    if form.is_valid():
      new_course= form.save(commit= False)
      new_course.category= category
      new_course.save()
      return HttpResponseRedirect(reverse('udemyx:course_detail', args=[new_course.id, new_course.slug]))
  return render(request, 'udemyx/new_course.html', {'category': category, 'form': form})  
  #return render(request, 'udemyx/test.html', {'category': category})

def course_list(request, category_slug= None):
  #return HttpResponse('<h1>Hello</h1>')
  
  category= None
  categories= Category.objects.all()
  courses   = Course.objects.all()
  if category_slug:
    category= get_object_or_404(Category, slug= category_slug)
    courses = courses.filter(category= category)
  return render(request, 'udemyx/courses_list.html', {'category': category, 'categories': categories, 'courses': courses})


def categories(request):
  categories= Category.objects.all()
  return render(request, 'udemyx/categories.html', {'categories': categories})

'''
def courses(request, category_id):
  category= get_object_or_404(Category, id= category_id)
  courses = Course.objects.filter(category= category)
  return render(request, 'udemyx/courses.html', {'category': category, 'courses': courses})  
'''


def course_detail(request, course_id, slug):
  course= get_object_or_404(Course, id= course_id, slug= slug)
  return render(request, 'udemyx/course_detail.html', {'course': course})


#def new_course(request, category_id):
  #return HttpResponse('<h1>Yahoo!</h1>')
  #return render(request, 'udemyx/test.html')
  '''
  category= get_object_or_404(Category, id= category_id)

  if request.method != "POST":
    form= CourseForm()
  else:
    form= CourseForm(request.POST)
    if form.is_valid():
      new_course= form.save(commit= False)
      new_course.category= category
      new_course.save()
      return HttpResponseRedirect(reverse('udemyx:courses', args=[category.id]))
  return render(request, 'udemyx/new_course.html', {'category': category, 'form': form})  
  '''



def edit_course(request, course_id):
  course= get_object_or_404(Course, id= course_id)
  category= course.category

  if request.method != 'POST':
    form= CourseForm(instance= course)
  else:
    form= CourseForm(instance= course, data= request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('udemyx:courses', args=[category.id]))
  context= {'category': category, 'form': form, 'course': course}      
  return render(request, 'udemyx/edit_course.html', context)  