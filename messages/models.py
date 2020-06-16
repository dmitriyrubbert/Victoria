# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MessageManager(models.Manager):
    def create(self, title):
        message = self.create(title=title)
        # do something with the message
        return message


class Message(models.Model):
    title = models.CharField(max_length=220)
    text = models.TextField()
    timestamp =  models.DateTimeField(auto_now=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    site_url = models.URLField()
    # https://docs.djangoproject.com/en/1.11/ref/contrib/postgres/fields/#jsonfield
    to_sent = models.CharField(max_length=220) # кому отправлено (json)

    objects = MessageManager()

    def __unicode__(self):
        return self.title

    class Meta:
    	ordering = ('title',)

# message = Message.objects.create("Hi!")