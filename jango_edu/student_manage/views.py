from requests import Response
from rest_framework import viewsets
from .models import StudentRecord, ExamRecord
from .serializers import StudentRecordSerializer, ExamRecordSerializer
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.db.models import Q
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class StudentRecordViewSet(viewsets.ModelViewSet):
    queryset = StudentRecord.objects.all()
    serializer_class = StudentRecordSerializer

class ExamRecordViewSet(viewsets.ModelViewSet):
    queryset = ExamRecord.objects.all()
    serializer_class = ExamRecordSerializer

    @action(detail=False, methods=['GET'], url_path='by-month/(?P<year>\d{4})/(?P<month>\d{1,2})', url_name='by_month')
    def by_month(self, request, year=None, month=None):
        # 해당 년도와 월에 해당하는 레코드만 필터링
        records = ExamRecord.objects.filter(
            Q(manage_date__year=year) & Q(manage_date__month=month)
        )

        # 월 기준으로 group by
        results = records.annotate(day=TruncDay('manage_date')) \
            .values('day') \
            .annotate(count=Count('id')) \
            .order_by('day')

        return Response(results)