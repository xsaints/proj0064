from django.db import models
from django.urls import reverse


class Category(models.Model):
  name = models.CharField(max_length= 120)
  description= models.TextField()

  class Meta:
    verbose_name_plural= 'Categories'

  def __str__(self):
    return self.name


class Product(models.Model):
  category= models.ForeignKey(Category, null= True, related_name= 'products', on_delete= models.SET_NULL)
  name = models.CharField(max_length= 500)
  slug = models.SlugField(default= "abc")
  description= models.TextField()
  price= models.DecimalField(max_digits= 12, decimal_places= 2, default= 1.00)
  image= models.ImageField(upload_to= 'images_uploaded/', default= 'static_proj/images/noimage.png', null= True, blank= True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('shop:product', kwargs= {'pk': self.pk})


class Country(models.Model):
  name= models.CharField(max_length= 200)
  country_code= models.PositiveIntegerField()


  def __str__(self):
    return self.name