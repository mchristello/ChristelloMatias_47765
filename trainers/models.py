from django.db import models
from pokemons.models import *



# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    favorite_type = models.CharField(max_length=20)
    owned_pokemons = models.ManyToManyField(Pokemon, blank=True)

    def __str__(self) -> str:
        return f"Name: {self.name} - Last Name: {self.lastname}"