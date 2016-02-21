from django.contrib import admin
from .models import Subject, Enrollment


class SubjectAdmin(admin.ModelAdmin):
    list_display=['id','name']

class EnrollmentAdmin(admin.ModelAdmin):
    list_display=['id','student','subject','grade']    

admin.site.register(Subject,SubjectAdmin)
admin.site.register(Enrollment,EnrollmentAdmin)