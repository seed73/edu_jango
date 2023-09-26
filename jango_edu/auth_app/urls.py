from django.urls import path
from .views import AccountListCreate

urlpatterns = [
    path('account/', AccountListCreate.as_view(), name='item-list-create'),
]