from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ItemListCreate

router = DefaultRouter()
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('', include(router.urls)),
]