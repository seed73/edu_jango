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
    created_at = models.DateTimeField(auto_now_add=True)  # 첫 생성시에만 현재 시간이 저장됩니다.
    updated_at = models.DateTimeField(auto_now=True)  # 매번 save()가 호출될 때마다 현재 시간으로 갱신됩니다.

    def __str__(self):
        return self.name