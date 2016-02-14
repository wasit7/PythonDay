from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Order
from django.http import HttpResponse
#from django.core.context_processors import csrf
#from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import rotate_token
import json
import sys

uname='wasit'
@ensure_csrf_cookie
def home(request):        
	rotate_token(request)
	return render(request,'home.html',{'uname': uname,})

#@csrf_exempt
def orders(request):	
	
	''' enable this section to see all data keys and values
		print >>sys.stderr, "Debug:: views.py::orders"
		for key, value in request.GET.iteritems() :
			print >>sys.stderr, "GET!!"
			print >>sys.stderr, key, value

		for key, value in request.POST.iteritems() :
			print >>sys.stderr, "POST!!"
			print >>sys.stderr, key, value
	'''
	if request.method == 'POST' and 'orders' in request.POST:	
		myorders=json.loads(request.POST.get('orders'))
		#print >>sys.stderr, "Debug:: views.py::orders>> myorders is %s"%(myorders)
		if 'orders' in myorders:
			#print >>sys.stderr, "Debug:: views.py::orders>> myorders['orders'] is %s"%(myorders['orders'])
			for i,d in enumerate( myorders['orders'] ):				
				rs = Order.objects.filter(customer__username=uname,product__name=d['name'])
				#print >>sys.stderr, "Debug:: views.py::orders>> i: %d len(rs) :%d %s"%(i,len(rs),d)
				if len(rs) == 1:
					rs[0].quantity=d['quantity']
					rs[0].save()					
				else: 
					return HttpResponse("ERROR views.py::orders() Found duplicated records")
			return HttpResponse("OK")

	if request.method == 'GET':
		orders=Order.objects.filter(customer__username=uname)
		data = {'orders':[{"name":i.product.name,"quantity":i.quantity} for i in orders]}
		return JsonResponse( data)
	return HttpResponse("Error")
	
def products(request):  
	products=Product.objects.all()
	data = {'products':[{"id":i.id,"name":i.name} for i in products]}
	return JsonResponse( data)