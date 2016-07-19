from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# For restricting view access use Mixins (Multiple Inheritance)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Booking
from .forms import BookingForm

class BookingListView(LoginRequiredMixin, ListView):
	model 			= Booking
	paginate_by 	= 10
	template_name 	= 'booking/booking_list.html'
	redirect_field_name = '/'


	def get(self, request, *args, **kwargs):
		obj 		= self.model.objects.all().order_by('-date')
		paginator 	= Paginator(obj, self.paginate_by) # show 1 contacts per page

		page = request.GET.get('page')

		try:
			bookings = paginator.page(page)
		except PageNotAnInteger:
			# If page not an integer, deliver first page
			bookings = paginator.page(1)
		except EmptyPage:
			# If page is out of rage (e.g. 99999), deliver last page of results
			bookings = paginator.page(paginator.num_pages)
		
		return render(request, self.template_name, {'obj_list': bookings})