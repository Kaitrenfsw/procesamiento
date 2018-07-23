# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-23 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0004_auto_20180524_2029'),
        ('new', '0003_auto_20180717_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='topic_id',
            field=models.ManyToManyField(related_name='topic_new', to='topic.Topic'),
        ),
    ]