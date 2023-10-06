from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExamRecordViewSet, StudentRecordViewSet

router = DefaultRouter()
router.register(r'stuedentRecord', StudentRecordViewSet)
router.register(r'examRecord', ExamRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]