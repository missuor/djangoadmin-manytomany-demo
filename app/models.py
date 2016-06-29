# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=30)
    managers = models.ManyToManyField(User, related_name='stations', blank=True)

    def __unicode__(self):
        return self.name
