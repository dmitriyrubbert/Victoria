# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
import json
from .utils import MaleParse, TemplateParse, CreateResponce

@ensure_csrf_cookie
def data(request, *args, **kwargs):
	''' get jsom data from chrome app '''
	if request.method == "POST":
		try:
			received_json_data = json.loads(request.body.decode('utf-8'))
			response_data = MaleParse(received_json_data)
		except Exception:
			response_data = {'result': 'error'}
		return JsonResponse(response_data)

@ensure_csrf_cookie
def template(request, *args, **kwargs):
	""" принимает шаблоны """
	if request.method == "POST":
		try:
			received_json_data = json.loads(request.body.decode('utf-8'))
			response_data = TemplateParse(received_json_data)
		except Exception:
			response_data = {'result': 'error'}
		return JsonResponse(response_data)

def home(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "home.html", {})

def responce(request, *args, **kwargs):
	""" отправляет список рассылки """
	return JsonResponse(CreateResponce)