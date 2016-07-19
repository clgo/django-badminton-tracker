from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, F
# For restricting view access use Mixins (Multiple Inheritance)
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Fund
from booking.models import Booking


class FundHistoryView(LoginRequiredMixin, ListView):
	model 				= Fund
	piginate_by 		= 10
	template_name 		= 'fund/fund_history.html'
	redirect_field_name = '/'

	def get(self, request, *args, **kwargs):
		fund_history 	= self.model.objects.all().order_by('-contrib_date')
		total		 	= self.model.objects.all().aggregate(total=Sum('contrib_amount'))
		obj 		 	= Booking.objects.filter(valid=True).aggregate(used=Sum(F('rate') * F('hour')))
		balance			= total['total'] - obj['used']
		paginator 		= Paginator(fund_history, self.paginate_by) # show 1 contacts per page

		page 			= request.GET.get('page')

		try:
			funds = paginator.page(page)
		except PageNotAnInteger:
			# If page not an integer, deliver first page
			funds = paginator.page(1)
		except EmptyPage:
			# If page is out of rage (e.g. 99999), deliver last page of results
			funds = paginator.page(paginator.num_pages)
		
		return render(request, self.template_name, {'obj_list': fund_history, 'total': total, 'funds': funds, 'balance': balance})