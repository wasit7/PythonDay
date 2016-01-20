'''shell
django-admin startproject mysite
python manage.py migrate
python manage.py createsuperuser --username=admin
'''

'''shell
python manage.py changepassword admin
'''

'''shell
python manage.py startapp my_app
'''

'''python
#\mysite\urls.py
from my_app import views
...
url(r'^$', views.home, name='home'),
'''

'''python
\mysite\my_app\views.py
from django.http import HttpResponse
from datetime import datetime
def home(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
'''