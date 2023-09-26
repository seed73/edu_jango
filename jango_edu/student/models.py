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
    enrollment_date = models.DateField() #등록일자
    is_enrolled = models.BooleanField(default=True) #등록상태
    mother_name = models.CharField(max_length=50, blank=True, null=True) #어머니 이름
    mother_phone_number = models.CharField(max_length=15, blank=True, null=True) #어머니 핸드폰번호
    father_name = models.CharField(max_length=50, blank=True, null=True) #아버지 이름
    father_phone_number = models.CharField(max_length=15, blank=True, null=True) #아버지 핸드폰번호

    def __str__(self):
        return self.name