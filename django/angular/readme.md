#AngularJS
##binding
##list
##dict

#Getting JSON from Django to AngularJS
##Create Project
```
	django-admi startproject sysite7
	cd mysite7
	python manage.py startapp myapp
```
##Create User table
```
		python manage.py migrate
		python manage.py createsuperuser --username=admin
```
##setting.py
```python
		INSTALLED_APPS = [
		    'django.contrib.admin',
		    'django.contrib.auth',
		    'django.contrib.contenttypes',
		    'django.contrib.sessions',
		    'django.contrib.messages',
		    'django.contrib.staticfiles',
		    'myapp',
		]
```
##edit views.py
	* create /static/angular.min.js
	* create /templates/index04.html
```html
		<!DOCTYPE html>
		<html>
		<head>
			<meta charset="utf-8">
			<title>Titile name</title>
			{% load staticfiles %}
			<script src="{% static 'angular.min.js' %}"></script>
		</head>	
		<body>

		{% verbatim %}
		<div ng-app='myApp' ng-controller='myCtrl'>
			<li ng-repeat='(key,value) in mydict'>
				Extension number for {{key}} in {{value}}.
			</li>
			Wasit's extension is {{mydict['Wasit']}}
		</div>
		{% endverbatim %} 

		<script>
		var app = angular.module('myApp', []);
		app.controller('myCtrl', function($scope,$http) {

			$http.get("{% url 'extension' %}")
		    .then(function(response) {
		        $scope.mydict = response.data;
		    });
		});
		</script>
		</body>
		</html>
```

##models.py
	Don't for get to makemigrations and  migrate after changing the models.py
```python
		from django.db import models
		class Extension(models.Model):
			name = models.CharField(max_length=10)
			extension=models.CharField(max_length=5)
```	

##admin.py
```python
		from django.contrib import admin
		from models import Extension

		class ExtensionAdmin(admin.ModelAdmin):
			list_display=['name','extension']

		admin.site.register(Extension, ExtensionAdmin)
```

##views.py
```python
		from django.shortcuts import render
		from models import Extension
		from django.http import JsonResponse
		# Create your views here.
		def index(request):
			return render(request, 'index04.html')

		def extension(request):
			ex = { i.name:i.extension for i in Extension.objects.all() }
			return JsonResponse(ex,safe=False)
```
##urls.py
```python
		from django.conf.urls import url
		from django.contrib import admin
		from myapp import views
		urlpatterns = [
		    url(r'^admin/', admin.site.urls),
		    url(r'^$', views.index, name='index'),
		    url(r'^extension.json', views.extension, name='extension'),
		]
```
#Posting JSON from AngularJS to Django
##Edit index05.html
###binding UI to mydict
###post mydict to server
##Edit views.py
###Add POST method
###get object and update