from django.core.management.base import BaseCommand
from lawdiff.tasks import convert_bill_text

class Command(BaseCommand):
    help = 'Convert bill details'
    def handle(self, *args, **options):
        convert_bill_text()
        self.stdout.write("Done.\n")
