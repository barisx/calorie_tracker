from django.db import models


# Create your models here.
class Food(models.Model):
    def __str__(self):
        return self.name  # Name fieldındaki değer obje adı olarak yansıyacak.

    name = models.CharField(max_length=100)
    calorie = models.FloatField(default=0)
    carb = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    pictureUrl = models.CharField(max_length=255)


class Consume(models.Model):
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)