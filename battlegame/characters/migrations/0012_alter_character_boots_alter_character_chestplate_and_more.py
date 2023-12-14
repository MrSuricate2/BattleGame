# Generated by Django 4.2 on 2023-04-07 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weapon', '0002_weapon_starter'),
        ('armor', '0004_alter_armor_options'),
        ('characters', '0011_alter_character_options_enemy_damage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='boots',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='armor.boots'),
        ),
        migrations.AlterField(
            model_name='character',
            name='chestplate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='armor.chestplate'),
        ),
        migrations.AlterField(
            model_name='character',
            name='helmet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='armor.helmet'),
        ),
        migrations.AlterField(
            model_name='character',
            name='leggings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='armor.leggings'),
        ),
        migrations.AlterField(
            model_name='character',
            name='state',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='tokens',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='weapon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='weapon.weapon'),
        ),
    ]