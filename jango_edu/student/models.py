from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    enrollment_date = models.DateField()
    is_enrolled = models.BooleanField(default=True)
    guardian_name = models.CharField(max_length=50, blank=True, null=True)
    guardian_phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name