# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 06:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('managers', models.ManyToManyField(blank=True, related_name='stations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]