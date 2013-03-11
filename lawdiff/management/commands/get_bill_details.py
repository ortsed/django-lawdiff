from django.core.management.base import BaseCommand
from lawdiff.tasks import get_bill_details

class Command(BaseCommand):
    help = 'Get bill details'
    def handle(self, *args, **options):
        get_bill_details()
        self.stdout.write("Done.\n")
