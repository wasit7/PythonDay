from django.contrib import admin
from models import Extension

class ExtensionAdmin(admin.ModelAdmin):
	list_display=['name','extension']

admin.site.register(Extension, ExtensionAdmin)
