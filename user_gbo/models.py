from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from urllib import request


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
    car_type = models.ForeignKey("CarType", on_delete=models.CASCADE, null=True, blank=True)
    car_marks = models.ForeignKey("CarMarks", on_delete=models.CASCADE, null=True, blank=True)
    car_model = models.ForeignKey("CarModels", on_delete=models.CASCADE, null=True, blank=True)
    gbo_in_car = models.IntegerField(choices=GBO_choice, default=0)


class CarType(models.Model):
    categoryID_choice = [
        (0, "Легковой"),
        (1, "Спецтехника"),
        (2, "Грузовик"),
        (3, "Автобус"),
        (4, "Автодом"),
    ]
    car_type = models.IntegerField(choices=categoryID_choice, default=0)


class CarMarks(models.Model):
    pass


class CarModels(models.Model):
    pass



# Create your models here.
