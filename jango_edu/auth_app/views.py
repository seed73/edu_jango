from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer

class AccountListCreate(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)