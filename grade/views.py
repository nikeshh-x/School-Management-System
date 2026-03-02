from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Class, Subject
from .forms import ClassForm, SubjectForm
# Create your views here.

def grade_list(request):
    classes = Class.objects.all()
    return render(request, 'grade/grade_list.html', {'classes':classes})

def grade_edit(request, pk):
    grade = get_object_or_404(Class, pk=pk)
    
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            messages.success(request, f'Class "{grade.name}" updated successfully!')
            return redirect('grade:list')
    else:
        form = ClassForm(instance=grade)
    
    # Get subjects for this class
    subjects = grade.subjects.all()
    
    return render(request, 'grade/grade_edit.html', {
        'grade': grade,
        'form': form,
        'subjects': subjects,
    })

def grade_delete(request, pk):
    grade = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        class_name = grade.name
        grade.delete()
        messages.success(request, f'Class "{class_name}" has been deleted successfully!')
        return redirect('grade:list')
    return render(request, 'grade/grade_delete.html', {'grade':grade,})