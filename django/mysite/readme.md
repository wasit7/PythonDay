Django Hello World!
---
1. Create a web app project called mysite and then create a table in a database. We also need a user. Here we create "username=admin" ```shell
django-admin startproject mysite
python manage.py migrate
python manage.py createsuperuser --username=admin
```
2. You may need to change the password. ```shell
python manage.py changepassword admin
```
3. Now, start the web app.```shell
python manage.py startapp my_app
```
4. Add your method in views.py```Python
#\mysite\my_app\views.py
from django.http import HttpResponse
from datetime import datetime
def home(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```
5. Dont forget to change the urls.py```Python
#\mysite\urls.py
from my_app import views
...
url(r'^$', views.home, name='home'),
```