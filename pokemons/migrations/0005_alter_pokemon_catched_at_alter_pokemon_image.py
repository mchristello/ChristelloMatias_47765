# Generated by Django 4.2.5 on 2023-09-28 01:24

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
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 27, 22, 24, 22, 402981)),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pokemon_img'),
        ),
    ]
