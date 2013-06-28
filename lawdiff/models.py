from django.db import models

from jsonmirror.models import JSON_Archive

class Bill(models.Model):

	json_archive = models.ForeignKey(JSON_Archive, null=False, blank=False, unique=True)
	
	json_details = models.TextField(blank=True, null=False)
	
	def __unicode__(self):
		return u"%s" % self.json_archive.__unicode__()
	
class Bill_File(models.Model):

	file = models.FileField(upload_to="bills")
	
	bill = models.ForeignKey(Bill)
	
	converted_bill_text = models.TextField(blank=True, null=False)
	
	parsed = models.BooleanField(default=False)

	def __unicode__(self):
		return u"%s" % self.file.name
