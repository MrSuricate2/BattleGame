# Generated by Django 4.2 on 2023-04-07 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typePersonnage', models.CharField(choices=[('Archer', 'Archer'), ('Magician', 'Magician'), ('Barbarian', 'Barbarian'), ('Paladin', 'Paladin')], default='Archer', max_length=25)),
                ('idPersonnage', models.IntegerField()),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
