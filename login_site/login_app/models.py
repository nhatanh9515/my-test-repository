# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# the reason that we should user User in auth.models is because
# it provides hashed password and other validations for username, etc.
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User)

    social_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username
