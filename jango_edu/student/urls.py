from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ItemListCreate

router = DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'item', ItemListCreate)

urlpatterns = [
    # path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('', include(router.urls)),
]