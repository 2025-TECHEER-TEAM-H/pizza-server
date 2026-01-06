# pizzas/serializers.py

from rest_framework import serializers
from .models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza        # 1. "Pizza 모델(재료)을 가지고"
        fields = '__all__'   # 2. "모든 정보를 다 JSON으로 포장해라"
