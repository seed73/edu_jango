from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class AccountManager(BaseUserManager):
    def create_user(self, email, user_id, name, phone_number, gender, entering_date, employment_status=True, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not user_id:
            raise ValueError('The given user_id must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            user_id=user_id,
            name=name,
            phone_number=phone_number,
            gender=gender,
            entering_date=entering_date,
            employment_status=employment_status,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_id, name, phone_number, gender, entering_date, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, user_id, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, user_id, name, phone_number, gender, entering_date, password=password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    entering_date = models.DateField()  # 입사일자
    employment_status = models.BooleanField(default=True)  # 재직상태
    email = models.EmailField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 첫 생성시에만 현재 시간이 저장됩니다.
    updated_at = models.DateTimeField(auto_now=True)  # 매번 save()가 호출될 때마다 현재 시간으로 갱신됩니다.

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # 관리자 사이트에 접근할 수 있는지 여부

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_id', 'name', 'phone_number', 'gender', 'entering_date']

    def __str__(self):
        return self.name

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their name
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        # Sends an email to this User.
        send_mail(subject, message, from_email, [self.email], **kwargs)