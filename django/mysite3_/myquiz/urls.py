from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^dotest/$', views.dotest, name='dotest'),
		url(r'^home/$', views.home, name='home'),
		url(r'^question/$', views.question, name='question'),
		url(r'^quiz/$', views.quiz, name='quiz'),
		url(r'^result/$', views.result, name='result'),
	]