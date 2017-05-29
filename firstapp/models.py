from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    position = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(null=True, blank=True, max_length=500)
    content = models.TextField(null=True, blank=True)
    TAG_CHOICES = (
        ('tech', 'Tech'),
        ('life', 'Life')
    )
    tag = models.CharField(null=True, blank=True, max_length=10, choices=TAG_CHOICES)

    def __str__(self):
        return self.headline

class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    comment = models.TextField()
    belong_to = models.ForeignKey(to=Article, related_name='under_comment', null=True, blank=True)
    best_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.comment
