# pizzas/views.py

from rest_framework import viewsets
from .models import Pizza
from .serializers import PizzaSerializer

# 클래스 이름이 'PizzaViewSet' 이어야 합니다! (대소문자 중요)
class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer