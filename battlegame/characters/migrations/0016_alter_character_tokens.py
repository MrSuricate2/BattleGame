# Generated by Django 4.2 on 2023-04-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0015_character_tokensavailable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='tokens',
            field=models.JSONField(default=dict),
        ),
    ]
