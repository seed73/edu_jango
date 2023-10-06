from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import ExamRecordViewSet, StudentRecordViewSet

router = DefaultRouter()
router.register(r'stuedentRecord', StudentRecordViewSet)
router.register(r'examRecord', ExamRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # re_path(r'^examRecord/(?P<year>\d+)/(?P<month>\d+)/$', ExamRecordViewSet.as_view({'get': 'list'}), name='examrecord-by-month'),
]