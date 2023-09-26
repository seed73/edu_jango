from django.urls import path
from .views import ItemListCreate, StudentListCreate

urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('student/', StudentListCreate.as_view(), name='item-list-create'),
]