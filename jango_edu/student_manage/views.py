from rest_framework import viewsets
from .models import StudentRecord, ExamRecord
from .serializers import StudentRecordSerializer, ExamRecordSerializer

# Create your views here.
class StudentRecordViewSet(viewsets.ModelViewSet):
    queryset = StudentRecord.objects.all()
    serializer_class = StudentRecordSerializer

class ExamRecordViewSet(viewsets.ModelViewSet):
    queryset = ExamRecord.objects.all()
    serializer_class = ExamRecordSerializer