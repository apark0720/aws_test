from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@univentures.co", "123456")
            self.stdout.write(self.style.SUCCESS(
                'Successfully created new super user'))
