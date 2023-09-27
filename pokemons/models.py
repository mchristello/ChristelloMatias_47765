from django.db import models
from datetime import datetime

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    attack = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    catched_at = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='static/img/', null=True, blank=True)

    def __str__(self) -> str:
        return f"Pokemon Name: {self.name}"