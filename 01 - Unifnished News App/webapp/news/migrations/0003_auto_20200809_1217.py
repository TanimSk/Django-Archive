# Generated by Django 3.1 on 2020-08-09 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200809_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='body_contect',
            new_name='body_content',
        ),
    ]