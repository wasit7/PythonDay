from django.contrib import admin
from .models import Musician, Album


Admin.site.register(Musician,Album)