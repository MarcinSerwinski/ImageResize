from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'images'

router = DefaultRouter()

router.register(r'images', views.ImageViewSet, basename='images')

urlpatterns = router.urls
