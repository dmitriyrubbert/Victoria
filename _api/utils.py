# -*- coding: utf-8 -*-
from .models import Female, Male, Template
import datetime, random

def GetUniqueTemplate(female_id, male_id):
	""" выборка уникального сообщения """
	responce = {}
	template_list = Template.objects.filter(
		female__id_user=female_id).exclude(male__id_user=male_id)
	if template_list.exists():
		template = random.choice(template_list)
		responce [male_id] = template.content

	return responce

def UpdateFields(obj, item):
	obj.name = item['name']
	obj.id_user = item['id']
	obj.age = item['age']
	obj.country = item['country']
	obj.last_visit = datetime.datetime.strptime(item['last_visit'], "%Y-%m-%d %H:%M:%S")
	obj.is_premium = item['is_premium']
	obj.is_online = item['is_online']
	obj.save()

def MaleParse(received_json_data):
	""" принимает ответ сайта при поиске + профиль девушки """
	received = 0
	users = received_json_data['data']['users']
	female_id = received_json_data['data']['female_id']
	responce = {}

	for item in users:
		# get_or_create Male
		obj, created = Male.objects.get_or_create(id_user=item['id'])
		# update fields
		UpdateFields(obj, item)
		# выборка уникального сообщения
		key_val = GetUniqueTemplate(female_id, obj.id_user)
		responce.update(key_val) 

		if created:
			received += 1

	return {'result': True, 'received': received, 'data': responce}

def TemplateParse(received_json_data):
	"""  принимает шаблоны сообщений от апплета """
	received = 0
	id_user = received_json_data['profile']['id_user']
	name = received_json_data['profile']['name']
	# поиск Female по id
	female, created = Female.objects.get_or_create(id_user=id_user, name=name)

	for item in received_json_data['templates']:
		obj, created = Template.objects.get_or_create(content=item, 
			female=female)

		if created:
			obj.save()
			received += 1

	return {'result': True, 'received': received}

def ProfileParse(received_json_data):
	""" должен обновлять профиль девушки """
	received = 0
	id_user = received_json_data['data']['list'][0]['id_user']
	name = received_json_data['data']['list'][0]['name']

	for item in received_json_data['data']['list'][0]:
		obj, created = Female.objects.get_or_create(name=name, 
			id_user=id_user)

		obj.age = item['age']
		obj.country = item['country']
		obj.city = item['city']
		obj.gender = item['gender']
		obj.occupation = item['occupation']
		obj.description = item['description']
		obj.avatar_xxs = item['avatar_xxs']
		obj.avatar_xl = item['avatar_xl']
		obj.avatar_large = item['avatar_large']
		obj.avatar_small = item['avatar_small']
		obj.audioEnabled = item['audioEnabled']
		obj.count_photos = item['count_photos']
		obj.count_videos = item['count_videos']
		obj.credits_premium = item['credits_premium']
		obj.credits_free = item['credits_free']
		obj.is_online = item['is_online']
		obj.last_visit = item['last_visit']



		obj.save()
		if created:
			received += 1

	return {'result': True, 'received': received}

def CreateResponce(received_user_list):
	""" отправить мужикам из списка новое сообщение  """
	for item in received_user_list:
		print item['id'], item['name']

	return {'result': True}


