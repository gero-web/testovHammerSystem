# Generated by Django 4.2.4 on 2023-08-20 00:40

import custom_user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='invate',
            field=models.CharField(default=custom_user.models.random_string, max_length=6),
        ),
    ]