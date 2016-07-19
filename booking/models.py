from django.db import models

COURT_NUMBER = (
		('1', 'Court 1'),
		('2', 'Court 2'),
		('3', 'Court 3'),
		('4', 'Court 4'),
		('5', 'Court 5'),
		('6', 'Court 6'),
	)


class Booking(models.Model):

	date 		= models.DateTimeField('Booking Date')
	rate		= models.DecimalField('Booking Rate/Hour', max_digits=12, decimal_places=2, default='4.0')
	hour		= models.IntegerField('No. Of Hours', default=3)
	court		= models.CharField('Court Number', max_length=2, choices=COURT_NUMBER)
	location	= models.CharField('Location', max_length=100, default='Republic Poly')
	valid		= models.BooleanField('Valid Booking', default=True)


	def __str__(self):
		return ("%s: Court %s on %s from %s for %i Hours" %(self.location, dict(COURT_NUMBER).get(self.court), self.date.strftime('%b %d, %Y (%a)'), self.date.strftime('%I:%M:%S %p'), self.hour))