# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-23 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicuser',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]