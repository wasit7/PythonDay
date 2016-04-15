from __future__ import unicode_literals

from django.db import models
class Extension(models.Model):
	name = models.CharField(max_length=10)
	extension=models.CharField(max_length=5)