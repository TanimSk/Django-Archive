# Generated by Django 3.1 on 2020-08-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200809_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_start',
            name='number',
            field=models.CharField(max_length=13),
        ),
    ]
