from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	# adding bootstrap formatting into the Django Model Form
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
					'class': 'form-control'
				})
			self.fields[field].help_text = None # to disable django form to automatic display help text in html

	def clean(self):
		username 	= self.cleaned_data.get('username')
		password 	= self.cleaned_data.get('password')
		user 		= authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
		return self.cleaned_data

	class Meta:
		model = User
		fields = ['username', 'password']