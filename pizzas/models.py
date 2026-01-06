# pizzas/models.py

from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=50) # 피자 이름 (최대 50글자)
    price = models.IntegerField()          # 가격 (숫자)

    # (선택사항) 관리자 페이지에서 "Pizza object(1)" 대신 이름으로 보이게 하는 마법
    def __str__(self):
        return self.name
