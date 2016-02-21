from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Subject(models.Model):
	name = models.CharField(max_length=6)
	def __unicode__(self):
		return unicode(self.name)

class Enrollment(models.Model):
	student=models.ForeignKey(
		User,
		on_delete=models.CASCADE,
	)
	subject=models.ForeignKey(
		Subject,
		on_delete=models.CASCADE,
	)
	grade=models.CharField(max_length=2)
	def __unicode__(self):
		return unicode(self.student.username)