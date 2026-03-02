from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=20)  # "1", "2", "3", "Kindergarten", etc.
    order = models.PositiveIntegerField(default=0)  # For sorting (1,2,3...)
    class_teacher = models.CharField(max_length=50, default='Nikeshh',blank=True)
    
    class Meta:
        ordering = ['order']  # Sort by order field
        verbose_name_plural = "Classes"
    
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=25)
    subject_code = models.CharField(max_length=20)
    of_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True, related_name='subjects')
    teacher = models.CharField(max_length=50, default='Demo Teacher',blank=True)

    def __str__(self):
        return f'{self.name} - {self.subject_code}'
    