# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    submitted_by = models.ForeignKey(User)
    upvotes = models.ManyToManyField(User, related_name='votes')
    submitted_on = models.DateTimeField(auto_now_add=True, editable=False)

class Comment(models.Model):
    body = models.TextField()
    commented_on = models.ForeignKey(Link)
    in_reply_to = models.ForeignKey('self', null=True)
    commented_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
