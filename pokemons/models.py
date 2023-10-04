from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    attack = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    catched_at = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='pokemones', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pokemons', null=True)
    

    def __str__(self) -> str:
        return f"Name: {self.name} || Catched At: {self.catched_at.strftime('%d-%m-%Y - %H:%M')}"
    
    def owner_email(self):
        return self.owner.email