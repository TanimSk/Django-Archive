# Generated by Django 3.1 on 2020-08-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200809_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_info',
            name='about',
            field=models.TextField(default=' '),
        ),
    ]
