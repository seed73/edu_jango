from django.db import models

# Create your models here.

class Account(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    entering_date = models.DateField() #입사일자
    employment_status= models.BooleanField(default=True) #재직상태
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name