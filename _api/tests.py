# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

// POST DATA CRF

var http = new XMLHttpRequest();
var url = "http://127.0.0.1:8000/data/";
var params = JSON.stringify( {obj:{int:12,str:"text",bool:true,null:null}} );
http.open("POST", url, true);

http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
http.setRequestHeader("X-CSRFToken", csrftoken);

'Access-Control-Allow-Origin'

http.onreadystatechange = function() {
    if(http.readyState == 4 && http.status == 200) {
        console.log( http.responseText );
    }
};
http.send(params);


-------

// TEMPLATE

var params = JSON.stringify({"templates":["helolo","hello2"],"profile":{"id_user":1671492,"name":"Inna"}});
var http = new XMLHttpRequest();
var url = "http://127.0.0.1:8000/template/";
http.open("POST", url, true);
http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
http.onreadystatechange = function() {
    if(http.readyState == 4 && http.status == 200) {
        console.log( http.responseText );
    }
};
http.send(params);

//profile

var params = JSON.stringify({"data":{"list":[{"id":1671492,"id_user":1671492,"name":"Inna","age":30,"country":"Ukraine","city":"Kharkiv","gender":"female","occupation":"teacher","description":"Communication with people is of great importance for me because I am very sociable and easy-going person. I have a lot of friends with whom I always share my problems and my victories. I love them and highly appreciate our friendship. I have an optimistic outlook, though sometimes it can\u2019t help me to overcome some difficulties or problems. I am a winsome and stylish girl with big kind heart and active and generous nature.","avatar_xxs":"https:\/\/ni.onthe.io\/shpzkl136b31ajcgfg.r35x35.16bb7ae8.jpg","avatar_xl":"https:\/\/ni.onthe.io\/shpzkl136b31ajcgfg.r220x200.db7b08f1.jpg","avatar_large":"https:\/\/ni.onthe.io\/shpzkl136b31ajcgfg.r100x100.78889228.jpg","avatar_small":"https:\/\/ni.onthe.io\/shpzkl136b31ajcgfg.r50x50.f2a1d352.jpg","audioEnabled":1,"count_photos":16,"count_videos":"1","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":true,"id_partner":"0","can_receive_gift":1,"mirrorName":"VictoriaBrides","mirrorCodes":["vb","vh","vt","ls"],"last_visit":"2017-09-06 19:44:21"}]}});
var http = new XMLHttpRequest();
var url = "http://127.0.0.1:8000/template/";
http.open("POST", url, true);
http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
http.onreadystatechange = function() {
    if(http.readyState == 4 && http.status == 200) {
        console.log( http.responseText );
    }
};
http.send(params);

// DATA

var params = JSON.stringify({"data":{"users":[{"id":1605110,"id_user":1605111,"name":"Nataniel","age":28,"country":"Netherlands","city":"Amsterdam","gender":"male","occupation":"","description":"","looking_for":"","avatar_xxs":"https://i.gstatvb.com/shpzkl3kmij61ihd0g.r35x35.7c3e3cf3.jpg","avatar_xl":"https://i.gstatvb.com/shpzkl3kmij61ihd0g.r220x200.5a688dce.jpg","avatar_large":"https://i.gstatvb.com/shpzkl3kmij61ihd0g.r100x100.f3e21330.jpg","avatar_small":"https://i.gstatvb.com/shpzkl3kmij61ihd0g.r50x50.d089e388.jpg","audioEnabled":1,"count_photos":1,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"0","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaBrides","mirrorCodes":"vb","last_visit":"2017-12-07 10:22:08"},{"id":2604621,"id_user":2604621,"name":"Антон","age":28,"country":"United States","city":"Moscow","gender":"male","occupation":"","description":"","looking_for":"","avatar_xxs":"https://i.gstatvb.com/shpzkl5g7rh9dkd3q.r35x35.a8800821.jpg","avatar_xl":"https://i.gstatvb.com/shpzkl5g7rh9dkd3q.r220x200.29a0d6d6.jpg","avatar_large":"https://i.gstatvb.com/shpzkl5g7rh9dkd3q.r100x100.b86bf946.jpg","avatar_small":"https://i.gstatvb.com/shpzkl5g7rh9dkd3q.r50x50.a0b89952.jpg","audioEnabled":0,"count_photos":5,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"0","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaBrides","mirrorCodes":"vb","last_visit":"2017-11-28 16:19:28"},{"id":5958652,"id_user":5958652,"name":"Albert","age":27,"country":"Russia","city":"St Petersburg","gender":"male","occupation":"Художник","description":"","looking_for":"","avatar_xxs":"https://i.gstatvb.com/shpzklabua9ad50qg.r35x35.c81e5e23.jpg","avatar_xl":"https://i.gstatvb.com/shpzklabua9ad50qg.r220x200.6cb5593e.jpg","avatar_large":"https://i.gstatvb.com/shpzklabua9ad50qg.r100x100.5b488c5d.jpg","avatar_small":"https://i.gstatvb.com/shpzklabua9ad50qg.r50x50.6083803f.jpg","audioEnabled":1,"count_photos":4,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"vh_nuu","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaHearts","mirrorCodes":"vh","last_visit":"2017-12-07 10:08:33"},{"id":6434754,"id_user":6434754,"name":"Phillip","age":27,"country":"Russia","city":"Moscow","gender":"male","occupation":"","description":"Hello my name is Phillip. I live in Moscow city. I'm shop manager","looking_for":"","avatar_xxs":"https://i.gstatvb.com/shpzkl2q3b723o69dg.r35x35.8804434b.jpg","avatar_xl":"https://i.gstatvb.com/shpzkl2q3b723o69dg.r220x200.82647cb5.jpg","avatar_large":"https://i.gstatvb.com/shpzkl2q3b723o69dg.r100x100.cff82fb6.jpg","avatar_small":"https://i.gstatvb.com/shpzkl2q3b723o69dg.r50x50.227dfc31.jpg","audioEnabled":1,"count_photos":1,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"0","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaBrides","mirrorCodes":"vb","last_visit":"2017-11-29 09:37:56"},{"id":6781506,"id_user":6781506,"name":"Pedro","age":32,"country":"Russia","city":"Moscow","gender":"male","occupation":"","description":"","looking_for":"","avatar_xxs":"https://i.gstatvb.com/shpzkl3pdtumfr3m4g.r35x35.530c3159.jpg","avatar_xl":"https://i.gstatvb.com/shpzkl3pdtumfr3m4g.r220x200.e57e04db.jpg","avatar_large":"https://i.gstatvb.com/shpzkl3pdtumfr3m4g.r100x100.767d060c.jpg","avatar_small":"https://i.gstatvb.com/shpzkl3pdtumfr3m4g.r50x50.83928a3e.jpg","audioEnabled":1,"count_photos":1,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"0","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaBrides","mirrorCodes":"vb","last_visit":"2017-12-05 22:31:42"},{"id":7074558,"id_user":7074558,"name":"Vladik","age":18,"country":"Russia","city":"","gender":"male","occupation":"","description":"","looking_for":"","avatar_xxs":"https://i.gstatvb.com/shpzkl4dnuosn50s6.r35x35.8622ebbf.jpg","avatar_xl":"https://i.gstatvb.com/shpzkl4dnuosn50s6.r220x200.bf84a140.jpg","avatar_large":"https://i.gstatvb.com/shpzkl4dnuosn50s6.r100x100.6082e0f4.jpg","avatar_small":"https://i.gstatvb.com/shpzkl4dnuosn50s6.r50x50.e09f5378.jpg","audioEnabled":1,"count_photos":1,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"1020n","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaBrides","mirrorCodes":"vb","last_visit":"2017-12-03 20:46:44"},{"id":7297747,"id_user":7297747,"name":"Ivan","age":28,"country":"Russia","city":"Mojaysk","gender":"male","occupation":"","description":"","looking_for":"","avatar_xxs":"https://i.gstatvb.com/shpzkl44qf9qokhs4.r35x35.c4777e62.jpg","avatar_xl":"https://i.gstatvb.com/shpzkl44qf9qokhs4.r220x200.da59334c.jpg","avatar_large":"https://i.gstatvb.com/shpzkl44qf9qokhs4.r100x100.37bd9c59.jpg","avatar_small":"https://i.gstatvb.com/shpzkl44qf9qokhs4.r50x50.d39b1866.jpg","audioEnabled":1,"count_photos":1,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"email_partner1_not_valid","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaBrides","mirrorCodes":"vb","last_visit":"2017-11-30 00:45:56"},{"id":7440161,"id_user":7440161,"name":"Takwa","age":21,"country":"Russia","city":"Moscow","gender":"male","occupation":"Student ","description":"I'm simple, honest, loyal person. And serious about commitment. ","looking_for":"","avatar_xxs":"https://i.gstatvb.com/shpzkl2ppcdfp4trlg.r35x35.288afeb5.jpg","avatar_xl":"https://i.gstatvb.com/shpzkl2ppcdfp4trlg.r220x200.6ca5731b.jpg","avatar_large":"https://i.gstatvb.com/shpzkl2ppcdfp4trlg.r100x100.09aaeba4.jpg","avatar_small":"https://i.gstatvb.com/shpzkl2ppcdfp4trlg.r50x50.564546b3.jpg","audioEnabled":1,"count_photos":1,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"0","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaHearts","mirrorCodes":"vh","last_visit":"2017-11-29 22:59:14"},{"id":7441392,"id_user":7441392,"name":"Roman","age":30,"country":"Ukraine","city":"Kiyv","gender":"male","occupation":"","description":"","looking_for":"","avatar_xxs":"https://i.gstatvb.com/shpzkl4ir3cguvvjv.r35x35.93585d1a.jpg","avatar_xl":"https://i.gstatvb.com/shpzkl4ir3cguvvjv.r220x200.131a773b.jpg","avatar_large":"https://i.gstatvb.com/shpzkl4ir3cguvvjv.r100x100.ff5b60fe.jpg","avatar_small":"https://i.gstatvb.com/shpzkl4ir3cguvvjv.r50x50.7de0a6be.jpg","audioEnabled":1,"count_photos":1,"count_videos":"0","credits_premium":0,"credits_free":20,"is_online":false,"is_premium":false,"id_partner":"1020n","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaBrides","mirrorCodes":"vb","last_visit":"2017-11-28 08:47:25"},{"id":7467086,"id_user":7467086,"name":"Sergey","age":28,"country":"Russia","city":"Petropavlovsk-Kamchatsky","gender":"male","occupation":"","description":"","looking_for":"","avatar_xxs":"https://i.gstatvb.com/shpzkl63smtqce6tf.r35x35.5c574ee2.jpg","avatar_xl":"https://i.gstatvb.com/shpzkl63smtqce6tf.r220x200.c9a4e268.jpg","avatar_large":"https://i.gstatvb.com/shpzkl63smtqce6tf.r100x100.f3746bd5.jpg","avatar_small":"https://i.gstatvb.com/shpzkl63smtqce6tf.r50x50.0a33390b.jpg","audioEnabled":1,"count_photos":2,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"1020n_not_valid","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaBrides","mirrorCodes":"vb","last_visit":"2017-11-30 10:30:05"},{"id":7479609,"id_user":7479609,"name":"Alex","age":29,"country":"Russia","city":"Astrakhan","gender":"male","occupation":"","description":"","looking_for":"","avatar_xxs":"//gstatvb.com/img/defaults/avatar/dc5a01.png","avatar_xl":"//gstatvb.com/img/defaults/avatar/5154fa.png","avatar_large":"//gstatvb.com/img/defaults/avatar/c788bb.png","avatar_small":"//gstatvb.com/img/defaults/avatar/7ff124.png","audioEnabled":1,"count_photos":1,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"browser_link","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaBrides","mirrorCodes":"vb","last_visit":"2017-12-01 10:18:45"},{"id":7506505,"id_user":7506505,"name":"jack","age":19,"country":"Russia","city":"","gender":"male","occupation":"","description":"","looking_for":"","avatar_xxs":"//gstatvb.com/img/defaults/avatar/dc5a01.png","avatar_xl":"//gstatvb.com/img/defaults/avatar/5154fa.png","avatar_large":"//gstatvb.com/img/defaults/avatar/c788bb.png","avatar_small":"//gstatvb.com/img/defaults/avatar/7ff124.png","audioEnabled":1,"count_photos":1,"count_videos":"0","credits_premium":0,"credits_free":0,"is_online":false,"is_premium":false,"id_partner":"tf_top1_desk","can_receive_gift":0,"imbra_verification":0,"mirrorName":"VictoriaBrides","mirrorCodes":"vb","last_visit":"2017-12-03 13:31:22"}],"count":12,"female_id":12345}});
var http = new XMLHttpRequest();
var url = "http://127.0.0.1:8000/data/";
http.open("POST", url, true);
http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
http.onreadystatechange = function() {
    if(http.readyState == 4 && http.status == 200) {
        console.log( http.responseText );
    }
};
http.send(params);
