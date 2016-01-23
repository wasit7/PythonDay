Django Part 1: Authentication 
==
+ create project and database
```shell
		django-admin startproject mysite2
		python manage.py migrate
		python manage.py createsuperuser --username=admin
```

+ create app called myauthen
```python
        python manage.py startapp myauthen
```

+ add app to /mysite2/settings.py
```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'myauthen',
        ]
```

+ add app to /mysite2/urls.py
```python
        from django.conf.urls import url, include
        from django.contrib import admin
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^myauthen/', include('myauthen.urls')),
        ]
```

+ create /mysite2/myauthen/urls.py
```python
        from django.conf.urls import url
        from . import views

        urlpatterns = [
            url(r'^$', views.signin, name='signin'),
            url(r'^signout/$', views.signout, name='signout'),
            url(r'^index/$', views.index, name='index'),
            url(r'^home/$', views.home, name='home'),
            ] 	
```

+ create directory /mysite2/myauthen/templates and then add signin.html and home.html

+ finally, create edit the views.py

+ run server by manage.py
```sheel
        python manage.py runserver
```