# Generated by Django 4.2.13 on 2024-06-03 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_mod_alter_service_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='mods',
            field=models.ManyToManyField(to='main_app.mod'),
        ),
    ]
