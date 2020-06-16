Chat bot backend for www. victoriabrides.com

Краткое описание работы с API:
-------------------------------------------
# отправка csrf_token
# https://docs.djangoproject.com/en/1.11/ref/csrf/#ajax

Запрос на рассылку:
---------------------------------------------------
# ["data"]["users"] список мужчин (выдает сайт при поиске по фильтрам )
# + id девушки (нужен для идентификации пользователя рассылки)

Пример запроса:
----------------

{
  "data": {
    "users": [
      {
        "id": 7506505,
        "id_user": 7506505,
        "name": "jack",
        "age": 19,
        "country": "Russia",
        "city": "",
        "gender": "male",
        "occupation": "",
        "description": "",
        "looking_for": "",
        "avatar_xxs": "//gstatvb.com/img/defaults/avatar/dc5a01.png",
        "avatar_xl": "//gstatvb.com/img/defaults/avatar/5154fa.png",
        "avatar_large": "//gstatvb.com/img/defaults/avatar/c788bb.png",
        "avatar_small": "//gstatvb.com/img/defaults/avatar/7ff124.png",
        "audioEnabled": 1,
        "count_photos": 1,
        "count_videos": "0",
        "credits_premium": 0,
        "credits_free": 0,
        "is_online": false,
        "is_premium": false,
        "id_partner": "tf_top1_desk",
        "can_receive_gift": 0,
        "imbra_verification": 0,
        "mirrorName": "VictoriaBrides",
        "mirrorCodes": "vb",
        "last_visit": "2017-12-03 13:31:22"
      }
    ],
    "count": 1,
    "female_id": 12345
  }
}



Пример ответа:
-----------
# в ответ в формате 'id мужчины': 'уникальное сообщение для отправки'
# если не найдено уникальное сообщение мужчине (нет нового шаблона, ему уже все слали)
# он исключается из рассылки

{
  "result": true,
  "received": 0,
  "data": {
    "1605111": "helolo",
    "2604621": "rerere1",
    "5958652": "hello2"
  }
}


Отправка на сервер шаблонов сообщений: 
-----------------------------------

Пример запроса:
-----------

{
  "templates": [
    "helolo",
    "hello2"
  ],
  "profile": {
    "id_user": 1671492,
    "name": "Inna"
  }
}

Пример ответа:
-----------

{
  "result": true,
  "received": 1
}


Отправка на сервер отчета об отправке: 
-----------------------------------
# еще не сделано

Пример запроса:
-----------

{
  "data": {
    "type": "success",
    "details": {
      "message": {
        "id_user_to": 682,
        "id_user_from": 1671492,
        "type": "message",
        "time": 1502092476,
        "content": "{\"id\":0,\"message\":\"Are you here?\"}",
        "id": 741255531,
        "date_created": "2017-08-07 07:54:36",
        "target": 682,
        "id_dialog": 384440529,
        "status": "unread"
      },
      "profiles": {
        "682": {
          "avatar_xxs": "https://ni.onthe.io/shpzkl3etge99sl56g.r35x35.f4d93fcd.jpg",
          "avatar_xl": "https://ni.onthe.io/shpzkl3etge99sl56g.r220x200.c7b2fec0.jpg",
          "avatar_large": "https://ni.onthe.io/shpzkl3etge99sl56g.r100x100.d968cf35.jpg",
          "avatar_small": "https://ni.onthe.io/shpzkl3etge99sl56g.r50x50.aafb9612.jpg",
          "audioEnabled": 1,
          "name": "Nikolay",
          "description": "",
          "id": 650,
          "id_user": 682,
          "age": 29,
          "count_photos": 1,
          "count_videos": 0,
          "credits_premium": 0,
          "credits_free": 0,
          "occupation": "",
          "country": "",
          "city": "",
          "gender": "male",
          "is_online": false,
          "is_premium": false,
          "id_partner": "0"
        },
        "1671492": {
          "avatar_xxs": "https://ni.onthe.io/shpzkl136b31ajcgfg.r35x35.16bb7ae8.jpg",
          "avatar_xl": "https://ni.onthe.io/shpzkl136b31ajcgfg.r220x200.db7b08f1.jpg",
          "avatar_large": "https://ni.onthe.io/shpzkl136b31ajcgfg.r100x100.78889228.jpg",
          "avatar_small": "https://ni.onthe.io/shpzkl136b31ajcgfg.r50x50.f2a1d352.jpg",
          "audioEnabled": 1,
          "name": "Inna",
          "description": "Communication with people is of great importance for me because I am very sociable and easy-going person. I have a lot of friends with whom I always share my problems and my victories. I love them and highly appreciate our friendship. I have an optimistic outlook, though sometimes it can’t help me to overcome some difficulties or problems. I am a winsome and stylish girl with big kind heart and active and generous nature.",
          "id": 344847,
          "id_user": 1671492,
          "age": 30,
          "count_photos": 16,
          "count_videos": 1,
          "credits_premium": 0,
          "credits_free": 0,
          "occupation": "teacher",
          "country": "Ukraine",
          "city": "Kharkiv",
          "gender": "female",
          "is_online": true,
          "is_premium": true,
          "id_partner": "0"
        }
      }
    },
    "pixel": "javascript:void(0);",
    "errors": []
  }
}