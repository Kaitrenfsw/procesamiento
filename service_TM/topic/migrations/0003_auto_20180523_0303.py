# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-23 03:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_auto_20180523_0228'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='topicuser',
            unique_together=set([('user_id', 'topic_id')]),
        ),
    ]
