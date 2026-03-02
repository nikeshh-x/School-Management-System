from django.contrib import admin
from .models import Class, Subject

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'class_teacher']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name','subject_code','teacher','of_class']
    list_display_links = ['name']
    list_editable = ['subject_code', 'of_class']
    ordering = ['of_class',]