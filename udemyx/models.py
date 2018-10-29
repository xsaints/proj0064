from django.db import models
from django.urls import reverse

from django.utils.text import slugify


class Category(models.Model):
  name = models.CharField(max_length= 200)
  slug  = models.SlugField(max_length= 500, db_index= True)


  def get_absolute_url(self):
    return reverse('udemyx:courses_by_category', args=[self.slug])


  def __str__(self):
    return self.name



class Course(models.Model):
  title = models.CharField(max_length= 500, db_index= True)
  slug  = models.SlugField(max_length= 500, db_index= True)
  author= models.CharField(max_length= 100)
  image = models.ImageField(upload_to= 'courses', blank= True)
  category= models.ForeignKey(Category, related_name= 'courses', on_delete= models.CASCADE)
  description= models.TextField()
  date_created= models.DateTimeField(auto_now_add= True)
  date_updated= models.DateTimeField(auto_now= True)
  price= models.DecimalField(max_digits= 10, decimal_places= 2, default= 1.00)


  class Meta:
    ordering= ('title',)
    index_together= (('title', 'slug'),)

  def save(self, *args, **kwargs):
    self.slug= slugify(self.title)
    super(Course, self).save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('udemyx:course_detail', args=[self.id, self.slug])


  def __str__(self):
    return self.title





