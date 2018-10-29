from django.shortcuts import render

from .models import Cart

'''
def cart_home(request):
  #del request.session['cart_id']
  cart_id= request.session.get('cart_id', None)
  print(cart_id)
  if cart_id is None:
    print('create cart')
    cart_obj= Cart.objects.create(user= None)
    request.session['cart_id']= cart_obj.id
  else:
    print('cart id exists')
    print(cart_id)
    cart_obj= Cart.objects.get(id= cart_id)
  print(cart_obj.id)
  return render(request, 'cart/home.html', {})
'''

def cart_home(request):
  #del request.session['cart_id']  
  cart_id= request.session.get('cart_id', None)
  if cart_id is None:
    print('create new cart')
    #cart_obj= Cart.objects.create(user= None)
    cart_obj= Cart.objects.new(user= request.user)
    request.session['cart_id']= cart_obj.id
  else:
    print('cart exists')
    print(cart_id)  
    cart_obj= Cart.objects.get(id= cart_id)
  print(request.session.get('cart_id'))
  return render(request, 'cart/home.html', {})