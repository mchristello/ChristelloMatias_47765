# Generated by Django 4.2.5 on 2023-10-11 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0004_alter_pokemon_catched_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='catched_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 11, 18, 50, 37, 22412)),
        ),
    ]
