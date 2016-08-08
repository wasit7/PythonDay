from __future__ import unicode_literals

from django.db import models

class Extension(models.Model):
	name=models.CharField(max_length=20)
	number=models.CharField(max_length=5)
	class Meta:
		ordering = ('name','number')
