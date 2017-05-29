# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-29 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20170528_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='under_comment', to='firstapp.Article'),
        ),
    ]
