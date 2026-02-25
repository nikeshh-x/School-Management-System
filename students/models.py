from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True, blank=True)
    full_name = models.CharField(max_length=80)
    age = models.PositiveIntegerField(default=0)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    father_name = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    mother_occupation = models.CharField(max_length=50, blank=True, null=True)
    

    primary_email = models.EmailField(blank=True, null=True)
    secondary_email = models.EmailField(blank=True, null=True)
    primary_phone = models.CharField(
        max_length=10, 
        blank=True, null=True,
        validators=[
            MinLengthValidator(10, message='Phone number must be exactly 10 digits'),
            MaxLengthValidator(10, message='Phone number must be exactly 10 digits'),
            RegexValidator(regex=r'^\d{10}$',
                            message='Phone number must be exactly 10 digits(number only)'
            )
        ]
    )
    secondary_phone = models.CharField(
        max_length=10, 
        blank=True, null=True,
        validators=[
            MinLengthValidator(10, message='Phone number must be exactly 10 digits'),
            MaxLengthValidator(10, message='Phone number must be exactly 10 digits'),
            RegexValidator(regex=r'^\d{10}$',
                            message='Phone number must be exactly 10 digits(number only)'
            )
        ]
    )

    is_active = models.BooleanField(default=True)

    joined_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
