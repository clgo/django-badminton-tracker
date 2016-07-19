from django import forms
from django.forms import ModelForm

from .models import Booking

class BookingForm(ModelForm):
	class Meta:
		model 	= Booking
		fields 	= ['date', 'rate', 'hour', 'court', 'location',]