# Generated by Django 4.2.5 on 2023-10-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_pokemon_experience_pokemon_totalxp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(default=3),
        ),
    ]
