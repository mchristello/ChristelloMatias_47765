# Generated by Django 4.2.5 on 2023-10-03 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0006_alter_pokemon_catched_at_alter_pokemon_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='catched_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 13, 54, 5, 432816)),
        ),
    ]