from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Order
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import rotate_token
import json
import sys

uname='wasit'
#@ensure_csrf_cookie
def home(request):        
	rotate_token(request)
	return render(request,'home.html',{'uname': uname,})

def orders(request):	
	''' enable this section to see all data keys and values
		for key, value in request.POST.iteritems() :
			print >>sys.stderr, "POST!!"
			print >>sys.stderr, key, value
	'''
	if request.method == 'GET':
		orders=Order.objects.filter(customer__username=uname)
		data = {'orders':[{"name":i.product.name,"quantity":i.quantity} for i in orders]}
		return JsonResponse( data)

	if request.method == 'POST' and 'orders' in request.POST:	
		myorders=json.loads(request.POST.get('orders'))
		if 'orders' in myorders:
			for i,d in enumerate( myorders['orders'] ):				
				rs = Order.objects.filter(customer__username=uname,product__name=d['name'])
				if len(rs) == 1:
					rs[0].quantity=d['quantity']
					rs[0].save()					
				else: 
					return HttpResponse("ERROR views.py::orders() Found duplicated records")
			return HttpResponse("OK")	
	return HttpResponse("Error")
	
def products(request):  
	products=Product.objects.all()
	data = {'products':[{"id":i.id,"name":i.name} for i in products]}
	return JsonResponse( data)