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
            # 여기서 request.user는 인증된 사용자의 정보를 가집니다.
            # 예를 들어, request.user.username, request.user.email 등으로 접근 가능합니다.
            # 이 정보를 사용하여 레코드를 저장할 수 있습니다.
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer