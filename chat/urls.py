from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'chat/^$', views.ExtLogin, name='external'),
    url(r'statistics/^$', views.StatisticsView, name='home'),
    url(r'^$', views.ChatView, name='home'),
    
]