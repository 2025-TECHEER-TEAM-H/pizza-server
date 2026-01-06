# pizzas/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PizzaViewSet

router = DefaultRouter()
router.register(r'', PizzaViewSet) # API 주소 자동 생성기

urlpatterns = [
    path('', include(router.urls)),
]