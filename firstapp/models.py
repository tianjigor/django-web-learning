from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    position = models.CharField(null=True, blank=True, max_length=200)
