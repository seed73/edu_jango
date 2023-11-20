from rest_framework import generics, status, viewsets
from .models import Item, Student
from .serializers import ItemSerializer, StudentSerializer
from rest_framework.response import Response

# class ItemListCreate(generics.ListCreateAPIView):
class ItemListCreate(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
        
            # 생성된 인스턴스 수정
            item.description = item.description + ' test'
            item.save()  # 변경 사항 저장

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # 여기에 커스텀 필터 로직 추가
        # 예시: queryset = queryset.filter(name__contains=request.query_params.get('name', ''))

        token = request.META.get('HTTP_AUTHORIZATION', None)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer