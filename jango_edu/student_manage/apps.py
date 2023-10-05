from django.apps import AppConfig


class StudentManageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_manage'

    def ready(self):
        import student_manage.signals