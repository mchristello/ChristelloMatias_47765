# Generated by Django 4.2.5 on 2023-09-28 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0002_alter_pokemon_catched_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='catched_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 27, 21, 40, 31, 131362)),
        ),
    ]
