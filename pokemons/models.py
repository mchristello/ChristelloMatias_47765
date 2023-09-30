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
    image = models.ImageField(upload_to='pokemon_img', null=True, blank=True)

    def __str__(self) -> str:
        return f"Name: {self.name} || Catched_at: {self.catched_at.strftime('%d-%m-%Y - %H:%M')}"