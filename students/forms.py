# students/forms.py
from django import forms
from .models import Student

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'student_id', 'age', 'date_of_birth', 'joined_date',
                 'father_name', 'father_occupation', 'mother_name', 'mother_occupation',
                 'primary_phone', 'secondary_phone','primary_email', 'secondary_email', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all'
            }),
            'joined_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all'
            }),
            'address': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': 'Enter full address...'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': 'John Doe'
            }),
            'student_id': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': 'STU001'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': '15'
            }),
            'father_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': "Father's full name"
            }),
            'father_occupation': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': 'Occupation'
            }),
            'mother_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': "Mother's full name"
            }),
            'mother_occupation': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': 'Occupation'
            }),
            'primary_phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': '5551234567'
            }),
            'secondary_phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': '5559876543'
            }),
            'primary_email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': 'john.doe@example.com'
            }),
            'secondary_email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all',
                'placeholder': 'alternate@example.com'
            })
        }
        labels = {
            'full_name': 'Full Name',
            'student_id': 'Student ID',
            'age': 'Age',
            'date_of_birth': 'Date of Birth',
            'joined_date': 'Joining Date',
            'father_name': "Father's Name",
            'father_occupation': "Father's Occupation",
            'mother_name': "Mother's Name",
            'mother_occupation': "Mother's Occupation",
            'primary_phone': 'Primary Phone',
            'secondary_phone': 'Secondary Phone',
            'primary_email': 'Primary Email',
            'secondary_email': 'Secondary Email',
            'address': 'Address',
        }
        help_texts = {
            'primary_phone': '10 digits only',
            'secondary_phone': '10 digits only (optional)',
            'student_id': 'Unique ID for the student',
        }