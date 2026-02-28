from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=20)  # "1", "2", "3", "Kindergarten", etc.
    order = models.PositiveIntegerField(default=0)  # For sorting (1,2,3...)
    class_teacher = models.CharField(max_length=50, default='Nikeshh')
    
    class Meta:
        ordering = ['order']  # Sort by order field
        verbose_name_plural = "Classes"
    
    def __str__(self):
        return self.name