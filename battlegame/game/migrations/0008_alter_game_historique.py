# Generated by Django 4.2 on 2023-04-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_alter_game_historique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='historique',
            field=models.JSONField(default=dict),
        ),
    ]
