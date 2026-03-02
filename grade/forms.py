from django import forms
from .models import Class, Subject

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'order', 'class_teacher']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all',
                'placeholder': 'Enter class name (e.g., 1, 2, Kindergarten)'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all',
                'placeholder': 'Enter order number for sorting',
                'min': '0'
            }),
            'class_teacher': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all',
                'placeholder': 'Enter class teacher name'
            }),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'subject_code', 'teacher']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all',
                'placeholder': 'Enter subject name'
            }),
            'subject_code': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all',
                'placeholder': 'Enter subject code'
            }),
            'teacher': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all',
                'placeholder': 'Enter teacher name'
            }),
        }
