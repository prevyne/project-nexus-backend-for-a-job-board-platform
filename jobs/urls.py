from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, JobViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]