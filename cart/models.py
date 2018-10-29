from django.db import models

from django.contrib.auth.models import User
from shop.models import Product



class CartManager(models.Manager):
  def new(self, user= None):
    print(user)
    user_obj= None
    if user is not None:
      if user.is_authenticated:
        user_obj= user
    return self.model.objects.create(user= user_obj)


class Cart(models.Model):
  user= models.ForeignKey(User, null= True, blank= True, on_delete= models.CASCADE)
  products= models.ManyToManyField(Product)
  total   = models.DecimalField(default= 0.00, max_digits= 20, decimal_places= 2)
  timestamp= models.DateTimeField(auto_now_add= True)
  updated  = models.DateTimeField(auto_now= True)

  objects= CartManager()


  def __str__(self):
    return str(self.id)

  '''
  def new(self, user= None):
    return self.models.objects.create(user= user)
  '''    