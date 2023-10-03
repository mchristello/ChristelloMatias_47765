from django.db import models

# Create your models here.
class Gym(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    master = models.CharField(max_length=150, blank=True, default='Available')

    def __str__(self) -> str:
        return f"Gym Name: {self.name}"