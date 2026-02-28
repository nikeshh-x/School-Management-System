from django.shortcuts import render
from .models import Class
# Create your views here.

def grade_list(request):
    classes = Class.objects.all()
    return render(request, 'grade/grade_list.html', {'classes':classes})