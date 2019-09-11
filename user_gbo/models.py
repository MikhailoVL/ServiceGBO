from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Gender_CHOICE = [
        (0, "Мужчина"),
        (1, "Женщина"),
        (2, "Другое"),
    ]
    GBO_choice = [
        (0, "Второе поколение"),
        (1, "третье поколение"),
        (2, "четвертое поколение"),
        (3, "пятое поколение"),
        (4, "шестое поколение"),
        (5, "седьмое поколение"),
    ]
    gender = models.IntegerField(choices=Gender_CHOICE, default=0)
    is_blocked = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=32, default="")
    auto_type = models.CharField(max_length=64)
    auto_marks = models.CharField(max_length=64)
    auto_model = models.CharField(max_length=64)
    gbo_in_car = models.IntegerField(choices=GBO_choice, default=0)


# Create your models here.
