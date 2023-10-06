from rest_framework import serializers
from .models import StudentRecord, ExamRecord

class StudentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRecord
        fields = '__all__'

class ExamRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamRecord
        fields = '__all__'