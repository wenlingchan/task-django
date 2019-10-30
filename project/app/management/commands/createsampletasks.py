from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import Task
from datetime import timedelta


class Command(BaseCommand):
    help = 'Create sample tasks for demonstration'

    def handle(self, *args, **options):
        Task.objects.get_or_create(title='Complete the spaceship', description='This is important because aliens will attack us very soon!', expiry_date=timezone.now() + timedelta(minutes=30))
        Task.objects.get_or_create(title='Drink something', description='Prefer coffee to tea.', expiry_date=timezone.now() - timedelta(minutes=30))
        Task.objects.get_or_create(title='Tell a joke', description='Try to make fun of myself.')
