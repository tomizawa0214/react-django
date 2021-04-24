from django.urls import path
from django.conf.urls import include
from rest_framework import routers

router = routers.Defaultrouter()

urlpatterns = [
    path('', include(router.urls),
]
