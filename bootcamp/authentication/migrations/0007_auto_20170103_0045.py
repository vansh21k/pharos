# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 00:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_lab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lab',
            old_name='user',
            new_name='manager',
        ),
    ]