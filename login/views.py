from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import View
from .forms import UserForm


class LoginView(View):
	form_class 		= UserForm
	template_name 	= 'login/login.html'

	# class based view default get request function, display a blank form
	def get(self, request):
		form = self.form_class(None) # clean form without data
		return render(request, self.template_name, {'form': form})

	# when user hits submit, a post request will automatically calls post method
	def post(self, request):
		form = self.form_class(request.POST)
		context = {
				"title": "Badminton Booking Tracker",
				"error_message": None,
		}
		user = authenticate(username=request.POST['username'], password=request.POST['password'])

		if user is not None:
			if user.is_active:
				login(request, user) # session is created after this
				return redirect('/booking')

		return render(request, self.template_name, {'form': form})

class LogoutView(View):
	"""
	Provides users the ability to logout
	"""
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(settings.LOGIN_URL)