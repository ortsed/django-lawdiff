from jsonmirror.models import JSON_Archive, JSON_Archive_Set
import json
import sunlight
import urllib
from lawdiff.models import Bill, Bill_File
from django.core.files.base import ContentFile

import pyPdf
from pyPdf.utils import PdfReadError
from BeautifulSoup import BeautifulSoup

from wordiff.models import ObjectGram
from wordiff.tasks import gram_parse_object_text

from sentry.client.models import client as sentry_client
import sys

def get_bill_details():

	json_objects = JSON_Archive.objects.filter(parsed=False)
	
	for json_object in json_objects:
		try:
			json_object_content = json.loads(json_object.content)
			bill = sunlight.openstates.bill(
				bill_id=json_object_content["id"],
			)
		
			bill = sunlight.openstates.bill(bill_id=json_object_content["id"],)
		
			local_bill = Bill()
			local_bill.json_details = json.dumps(bill)
			local_bill.json_archive = json_object
			local_bill.save()
	
			bill_file = Bill_File()
			bill_file.bill = local_bill
		
			if bill["documents"]:
				f = urllib.urlopen(bill["documents"][0]["url"])
				contents = f.read()
				file_name = f.url.split("/")[-1]
				f.close()
			
				file_contents = ContentFile(contents)
				bill_file.file.save(file_name, file_contents, save=True)
				
				bill_file.save()
			json_object.parsed = True	
			json_object.save()
		except:
			sentry_client.create_from_exception(exc_info=sys.exc_info(), data={})

def convert_pdf(path):
	content = ""
	f = file(path, "rb")
 	# Load PDF into pyPDF
	pdf = pyPdf.PdfFileReader(f)

	# Iterate pages
	for i in range(0, pdf.getNumPages()):
	# Extract text from page and add to content
		content += pdf.getPage(i).extractText() + "\n"
  
	soup = BeautifulSoup(content)
	return soup.contents[0]

def fixPdf(pdfFile):
	try:
		fileOpen = file(pdfFile, "a")
		fileOpen.write("%%EOF")
		fileOpen.close()
		return "Fixed"
	except Exception, e:
		sentry_client.create_from_exception(exc_info=sys.exc_info(), data={})
	
def convert_bill_text():

	bill_files = Bill_File.objects.filter(converted_bill_text="")[0:20]
	
	for bill_file in bill_files:
		try:
			bill_file.converted_bill_text = convert_pdf(bill_file.file.path)
			bill_file.save()
		except PdfReadError:
			fixPdf(bill_file.file.path)	
		except:
			sentry_client.create_from_exception(exc_info=sys.exc_info(), data={})	
def ngram_bill_text():
	bill_files = Bill_File.objects.filter(parsed=False)[0:20]
	for bill_file in bill_files:
		try:
			gram_parse_object_text(bill_file, bill_file.converted_bill_text)
			bill_file.parsed = True
			bill_file.save()
		except:
			sentry_client.create_from_exception(exc_info=sys.exc_info(), data={})

	
	
