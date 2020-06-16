# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from django.core.mail import send_mail

def test ():
	send_mail('Subject here', 'Here is the message.',
	          'admin@mydomain.com',['me@gmail.com'], fail_silently=False)
