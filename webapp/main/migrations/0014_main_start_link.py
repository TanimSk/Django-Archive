# Generated by Django 3.1 on 2020-08-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200809_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_start',
            name='link',
            field=models.TextField(default=' '),
        ),
    ]
