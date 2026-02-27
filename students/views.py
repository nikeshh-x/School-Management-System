from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentCreateForm
# Create your views here.

def student_list(request):
    students = Student.objects.filter(is_active=True)
    return render(request, 'students/student_list.html', {'students':students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student':student})

def student_create(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:list')
    else:
        form = StudentCreateForm()
    context = {
        'form':form,
        'is_edit': False,
        'title': 'Create New Student'
    }
    return render(request, 'students/student_form.html',context)

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentCreateForm(request.POST ,instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:list')
    else:
        form = StudentCreateForm(instance=student)
    context = {
        'form':form,
        'is_edit':True,
        'title':f'Edit Student:{student.full_name}'
    }
    return render(request, 'students/student_form.html',context)