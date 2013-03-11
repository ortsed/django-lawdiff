from django.core.management.base import BaseCommand
from lawdiff.tasks import ngram_bill_text

class Command(BaseCommand):
    help = 'Ngram Bill Text'
    def handle(self, *args, **options):
        ngram_bill_text()
        self.stdout.write("Done.\n")
