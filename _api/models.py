# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

class Female(models.Model):              # наши бабы
    name = models.CharField(max_length=30)
    id_user = models.CharField(max_length=15)
    is_member = models.BooleanField(default=False, 
                    verbose_name='Is Paid Member')
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0} id:{1}'.format(self.name, self.id_user)

    class Meta:
        ordering = ('name',)

class Template(models.Model):              # заготовки отправленные мужикам сайта
    content = models.CharField(max_length=220)
    pub_date = models.DateTimeField(auto_now_add=True) #when model was created
    updated = models.DateTimeField(auto_now=True) #everytime the model is saved
    # https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_one/
    female = models.ForeignKey(Female, related_name='template')
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0}'.format(self.content)[0:20]

    class Meta:
        ordering = ('updated',)

class Male(models.Model):              # мужики сайта
    name = models.CharField(max_length=30)
    id_user = models.CharField(max_length=15)

    age = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=30, null=True , blank=True)
    last_visit = models.DateTimeField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    #https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/
    template = models.ManyToManyField(Template, blank=True)

    def __unicode__(self):
        return '{0} id:{1}'.format(self.name, self.id_user)

    class Meta:
        ordering = ('id_user',)

# @receiver(pre_save, sender=Template)
# def template_callback(sender, instance, signal, *args, **kwargs):
#     instance.updated = timezone.now()
#     print "Request finished!", signal



# django no such table:
# python manage.py migrate --run-syncdb

# django no such column
# снеси таблицу или добавть столбцы руками


