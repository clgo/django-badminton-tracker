from django.db import models
from django.conf import settings # for user user  model

class Fund(models.Model):

	contrib_date		= models.DateTimeField('Fund Contribution Date')
	contrib_user		= models.ForeignKey(settings.AUTH_USER_MODEL)
	contrib_amount		= models.DecimalField('Contributed Amount $', max_digits=10, decimal_places=2)

	def __str__(self):
		return ("%s %s %s" %(self.contrib_user.last_name, self.contrib_user.first_name, self.contrib_date.strftime('%b %d, %Y')))