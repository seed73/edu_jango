from django.db import models

class StudentRecord(models.Model):
    # Primary key, id는 기본적으로 Django 모델에 포함되므로 별도로 정의할 필요가 없습니다.

    student_id = models.IntegerField(null=False, blank=True)
    manage_date = models.DateField(null=False, blank=True)
    current = models.TextField(null=True, blank=True) #현재
    remain_test_area = models.TextField(null=True, blank=True) #남은 시험범위
    comma = models.CharField(max_length=255, null=True, blank=True) #콤마
    school_grade_data = models.DateField(null=True, blank=True) #학교내신자료
    cm_backup = models.CharField(max_length=255, null=True, blank=True)  #cm백업
    individual_instruct_room = models.CharField(max_length=255, null=True, blank=True)  #개인지도실
    Textbook_explanation = models.BooleanField(default=False, null=True, blank=True)  # 교과서 풀이 여부
    etc = models.TextField(null=True, blank=True)  # 기타 정보를 위한 텍스트 필드

    # 아래는 시스템에 의해 관리되는 정보를 위한 필드입니다.
    created_by = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.student_id)  # student_id를 문자열로 반환하여 객체를 표현합니다.

# Create your models here.
class StudentRecordHistory(models.Model):
    student_record = models.ForeignKey(StudentRecord, on_delete=models.CASCADE, related_name='histories')
    changed_at = models.DateTimeField(auto_now_add=True)
    changes = models.TextField(null=True, blank=True)  # 변경 사항을 저장하는 필드. 필요에 따라서는 JSONField도 고려할 수 있습니다.
    updated_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Change at {self.changed_at} for Student {self.student_record.student_id}'

class ExamRecord(models.Model):
    student_id = models.IntegerField(null=False, blank=True)
    manage_date = models.DateField(null=False, blank=True)
    test_name = models.TextField(null=True, blank=True) #시험명
    subject_name = models.TextField(null=True, blank=True) #과목명
    grade = models.CharField(max_length=2, null=True, blank=True) #등급
    score = models.IntegerField(null=True, blank=True) #점수
    etc = models.TextField(null=True, blank=True) #메모

    # 아래는 시스템에 의해 관리되는 정보를 위한 필드입니다.
    created_by = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.student_id)  # student_id를 문자열로 반환하여 객체를 표현합니다.