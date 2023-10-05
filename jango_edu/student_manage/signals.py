from django.db.models.signals import post_save
from django.dispatch import receiver

from jango_edu.student_manage.models import StudentRecord, StudentRecordHistory

@receiver(post_save, sender=StudentRecord)
def save_history(sender, instance, **kwargs):
    if instance.pk:  # 새로 생성되는 객체가 아닌 기존 객체가 업데이트되었을 경우만
        # 실제로는 변경된 필드만 추출하여 기록하는 것이 좋습니다.
        # 아래의 예시는 모든 필드를 문자열로 변환하여 저장하는 단순한 예시입니다.
        changes = str(instance.__dict__)
        StudentRecordHistory.objects.create(student_record=instance, changes=changes, updated_by=instance.updated_by)