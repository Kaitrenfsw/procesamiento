# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-24 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TMengine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ldamodel',
            old_name='name',
            new_name='filename',
        ),
        migrations.RemoveField(
            model_name='ldamodel',
            name='in_use',
        ),
    ]
