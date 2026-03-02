from django.urls import path
from . import views

app_name = 'grade'

urlpatterns = [
    path('', views.grade_list, name='list'),
    path('edit/<int:pk>/', views.grade_edit, name='edit'),
    path('delete/<int:pk>/', views.grade_delete, name='delete'),
]
