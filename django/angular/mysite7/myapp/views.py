from django.shortcuts import render
from models import Extension
from django.http import JsonResponse
from django.http import HttpResponse
import json
import sys

def index(request):
	return render(request, 'index04.html')

def extension(request):
	ex = { i.name:i.extension for i in Extension.objects.all() }
	return JsonResponse(ex,safe=False)

def update(request):
	if request.method == 'GET':
		return render(request, 'index05.html')
	if request.method == 'POST':
		#print >>sys.stderr, request.body
		ex = json.loads(request.body)
		for k,v in ex.iteritems():
			record = Extension.objects.get(name=k)
			record.extension = v
			record.save()
		return HttpResponse("It's OK")
