from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product

class Command(BaseCommand):
    help = 'Load test products from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        call_command('loaddata', 'products_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))