from __future__ import unicode_literals
from django.db import models
# Create your models here.


class zad_cat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
