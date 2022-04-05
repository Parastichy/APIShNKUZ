from django.urls import path, include
from .views import BaseViewSet, index
from rest_framework import routers

router = routers.DefaultRouter()
router.register('API', BaseViewSet)


urlpatterns = [
    path('', index),
    path('base/', include(router.urls)),
]


