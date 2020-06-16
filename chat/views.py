# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.http import HttpResponse
from . import utils, forms
from accounts.models import MyUser, UserProfile

from grab import Grab

# декоратор,будет запрашивать логин на сайт
# если профиль содержит метку залогинен
    	# то пропустить

    	# иначе залогинить на сайте
    	# если успешно
    	# 	отправить на страницу поиска
def site_login_required(function):
    def wrap(request, *args, **kwargs):
        if utils.profile():
            return function(request, *args, **kwargs)
        else:
            return redirect('external')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def HomeView(request):
	context = {
	"banner": "Добро пожаловать!"
	}
	return render(request, "home.html", context) 

# @site_login_required
def ChatView(request):
		return render(request, "chat/chat.html", {"title": "Chat"}) 

def StatisticsView(request):
        return render(request, "accounts/statistics.html", {"title": "Statistics"}) 

def test_view(request):
    current_user = request.user
    # print dir(current_user)
    print current_user.is_authenticated
    return HttpResponse(current_user.id)

def ExtLogin(request):
    if request.method == 'POST':
        form = forms.AgencyLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # return HttpResponse('<center>Authenticated successfully</center>')
            grab=Grab(debug_post=True)
            result = utils.login(grab, cd['email'], cd['password'])
            return HttpResponse('<center>' + result + '</center>')

            # user = authenticate(username=cd['username'], password=cd['password'])
            # if user is not None:
            #     if user.is_active:
            #         login(request, user)
            #         return HttpResponse('Authenticated successfully')
            #     else:
            #         return HttpResponse('Disabled account')
            # else:
            #     return HttpResponse('Invalid login')
    else:
        form = forms.AgencyLoginForm()
    return render(request, 'accounts/ext-login.html', {'form': form})

# class ExtLogin(View):

# 	def get(self, request, *args, **kwargs):
# 		form = AgencyLoginForm()
# 		return render(request, "ext-login.html", {"form": form}) 

# 	def post(self, request, *args, **kwargs):
# 		# print(request.POST)
# 		# print(request.POST.get("url")) 
# 		form = AgencyLoginForm(request.POST)
# 		context = {
# 			"form": form
# 			}
# 		template = "ext-login.html"

# 		if form.is_valid():
# 			email = form.cleaned_data.get("email")
# 			password = form.cleaned_data.get("password")

	

# 			return HttpResponse( UserProfile.objects.get_or_create(grab_config))


# 			# save login passwd
# 			# доработать после создания модели пользователя
			
# 			# print(email,password)

# 			# авторизация граб
# 			# current_user = request.user
# 			# if current_user.is_authenticated():
# 			# 	current_user.grab_config = 'None'
# 			# 	# print dir(current_user)
# 			# 	print current_user.email
# 			# try:
# 		 #        user = User.objects.get(verification_uuid=uuid, is_verified=False)
# 		 #    except User.DoesNotExist:
# 		 #        raise Http404("User does not exist or is already verified")
		 
# 		 #    user.is_verified = True
# 		 #    user.save()
# 		 	# obj, created = User.objects.get_or_create(grab_config='empty')
# 		 	# if created:
# 		 	# 	print obj.grab_config

# 		 	# qs = User.objects.filter(email__iexact=email)
# 		 	# print qs.email

# 			context = {
# 			"password": password,
# 			"email" : email
# 			}
# 			if True:
# 				HttpResponse('профиль забрал')
# 				template = "chat/success.html"
# 			else:
# 				template = "chat/error.html"

		
# 		return render(request, template , context)

