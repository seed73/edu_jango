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
    age =  models.IntegerField(null=True)
    school_name = models.CharField(max_length=50)
    grade=  models.IntegerField(null=True)
    enrollment_date = models.DateField() #등록일자
    is_enrolled = models.BooleanField(default=True) #등록상태
    mother_name = models.CharField(max_length=50, blank=True, null=True) #어머니 이름
    mother_phone_number = models.CharField(max_length=15, blank=True, null=True) #어머니 핸드폰번호
    father_name = models.CharField(max_length=50, blank=True, null=True) #아버지 이름
    father_phone_number = models.CharField(max_length=15, blank=True, null=True) #아버지 핸드폰번호
    created_at = models.DateTimeField(auto_now_add=True)  # 첫 생성시에만 현재 시간이 저장됩니다.
    updated_at = models.DateTimeField(auto_now=True)  # 매번 save()가 호출될 때마다 현재 시간으로 갱신됩니다.

    def __str__(self):
        return self.name