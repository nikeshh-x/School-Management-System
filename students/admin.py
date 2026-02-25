from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','full_name','father_name', 'mother_name')
    list_display_links = ('full_name', 'student_id')
    search_fields = ('full_name', 'student_id')
    ordering = ('full_name',)
