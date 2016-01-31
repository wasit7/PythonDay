from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
import sys
import social.apps.django_app.default.models as sm
# Create your views here.
#@login_required(login_url='url_signin')
def home(request):
    #print >> sys.stderr, "_index user:%s"%request.user.username
    print >> sys.stderr, "Debug1:"
    for k,v in request.session.iteritems():
        print >> sys.stderr, "%s: %s\n"%(k,v)

    print >> sys.stderr, "Debug2:"
    for s in Session.objects.iterator():
            print >> sys.stderr, "%s\n"%s.get_decoded()


    if '_auth_user_id' in request.session:
        if request.session['_auth_user_backend']==u'django.contrib.auth.backends.ModelBackend':
            uname=request.session['user_username']
        else:
            uname=sm.UserSocialAuth.objects.get(user_id=int(request.session['_auth_user_id']))
    else:
        uname="Anonymous"
    
    
    return render(request,'home.html',{'msg': "Hello %s"%uname})

def question(request):
    return render(request,'question.html',{'msg': "Queation"})

def quiz(request):
    return render(request,'quiz.html',{'msg': "Quiz"})

def result(request):
    return render(request,'result.html',{'msg': "result"})

def dotest(request):
    return render(request,'dotest.html',{'msg': "result"})
