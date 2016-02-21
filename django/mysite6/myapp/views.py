from django.shortcuts import render
from .models import Subject, Enrollment
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
import sys
uname='wasit'
def home(request):
	return render(request,'home.html',{'uname': 'Wasit'})

def subjects(request):
	subjects=Subject.objects.all();
	data={'serverdata':[ {'subid':i.pk,'subname':i.name} for i in subjects] }
	return JsonResponse( data)
def remove_subjects(request):
	if request.method == 'POST':
		clientdata = json.loads(request.body)
		for d in clientdata:
			enroll=Enrollment.objects.filter(
				student__username=uname, 
				subject__name=d['subname']
			).delete()
	enroll_list=Enrollment.objects.filter(student__username=uname);
	data={'serverdata':[ {'subid':i.pk, 'subname': i.subject.name, 'grade':i.grade,} for i in enroll_list] }
	return JsonResponse( data)
def enrolls(request):
	print >>sys.stderr, "Debug!!"
	print >>sys.stderr, request.body
	
	if request.method == 'GET':
		enroll_list=Enrollment.objects.filter(student__username=uname);
		data={'serverdata':[ {'subid':i.pk, 'subname': i.subject.name, 'student':i.student.username, 'grade':i.grade,} for i in enroll_list] }
		return JsonResponse( data)
	if request.method == 'POST':
		clientdata = json.loads(request.body)
		print >>sys.stderr, clientdata
		for d in clientdata:
			print >>sys.stderr, d
			enroll=Enrollment.objects.filter(
				student__username=uname, 
				subject__name=d['subname']
			)
			if('grade' in d):
				mygrade=d['grade']
			else:
				mygrade='-'
			if(len(enroll)==1):
				old_enroll=Enrollment.objects.get(id=enroll[0].id)
				old_enroll.grade=mygrade
				old_enroll.save()
			if(len(enroll)==0):
				new_enroll=Enrollment(
					student=User.objects.get(username=uname),
					subject=Subject.objects.get(name=d['subname']),
					grade=mygrade,
				)
				new_enroll.save()
		enroll_list=Enrollment.objects.filter(student__username=uname);
		data={'serverdata':[ {'subid':i.pk, 'subname': i.subject.name, 'grade':i.grade,} for i in enroll_list] }
		return JsonResponse( data)