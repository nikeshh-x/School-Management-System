from django.urls import path
from . import views

app_name = 'grade'

urlpatterns = [
    path('', views.grade_list, name='list')
]
