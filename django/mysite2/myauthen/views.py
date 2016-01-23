from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
def signin(request):
    if request.method == 'POST' and 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print "password: %s"%password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_username'] = user.username
                print "username:%s"%user.username
                #return render(request,'index.html',{'msg': "Do something"})
                return redirect('home')
            else:
                msg="Disabled account"
        else:
            msg="Invalid login"
        return render(request,'signin.html',{'msg': msg})   
    return render(request,'signin.html',{'msg': "Please sign-in"})


def signout(request):
    if request.method == 'POST':
        print "signout"
        if 'user_username' in request.session:
            del request.session['user_username']
            print "del uname"
        logout(request)
    return render(request,'signin.html',{'msg': "Please sign-in"})


#@login_required(login_url='url_signin')
def home(request):
    print "_index user:%s"%request.user.username
    if 'user_username' in request.session:
        uname=request.session['user_username']
    else:
        uname="Anonymous"
    return render(request,'home.html',{'msg': "Hello %s"%uname})


from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello World!")