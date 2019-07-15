from django.conf.urls import url, include
from rest_framework import routers

from .views import JobViewSet


router = routers.DefaultRouter()
router.register(r'', JobViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
