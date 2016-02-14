from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)
    def __unicode__(self):
        return unicode(self.name)
        
class Order(models.Model):
    time = models.DateTimeField(auto_now=True)    
    product=models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    customer=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    quantity=models.IntegerField(default=0)
    

    