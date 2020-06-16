# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Female, Male, Template
class FemaleAdmin(admin.ModelAdmin):
    # fields = ['name', 'template']
    # fieldsets = [
    #     (None,               {'fields': ['name']}),
    #     ('Date information', {'fields': ['template'], 'classes': ['collapse']}),
    # ]
    list_display = ('name', 'id_user')
    list_filter = ['is_active', 'is_member']
    search_fields = ['name', 'id_user']
    # date_hierarchy = 'pub_date'

class MaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_user')
    list_filter = ['country', 'is_premium']
    search_fields = ['name', 'id_user']
    filter_horizontal = ('template',)

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('content', 'female', 'pub_date', 'updated')
    list_filter = ['female', 'pub_date']
    search_fields = ['content']
    date_hierarchy = 'pub_date'

admin.site.register(Female, FemaleAdmin)
admin.site.register(Male, MaleAdmin)
admin.site.register(Template, TemplateAdmin)

# useradmin gold H2Fe7ooU
# http://itman.in/django-admin-changes/
# https://djbook.ru/ch06s08.html