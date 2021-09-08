from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from hawc.apps.common.signals import ignore_signals


class Command(BaseCommand):
    help = """Load the test database from a fixture."""

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--ifempty",
            action="store_true",
            dest="ifempty",
            help="Only flush/load if database is empty",
        )

    def handle(self, *args, **options):

        if not any(_ in settings.DATABASES["default"]["NAME"] for _ in ["fixture", "test"]):
            raise CommandError("Must be using a test database to execute.")

        with ignore_signals():
            self.stdout.write(self.style.HTTP_INFO("Migrating database schema..."))
            call_command("migrate", verbosity=0)

            if options["ifempty"] and get_user_model().objects.count() > 0:
                message = "Migrations complete; fixture not loaded (db not empty)"
            else:
                self.stdout.write(self.style.HTTP_INFO("Flushing data..."))
                call_command("flush", verbosity=0, interactive=False)

                self.stdout.write(self.style.HTTP_INFO("Loading database fixture..."))
                call_command("loaddata", str(settings.TEST_DB_FIXTURE), verbosity=1)

                self.stdout.write(self.style.HTTP_INFO("Loading database views..."))
                call_command("create_views", verbosity=1)
                message = "Migrations complete; fixture loaded"

            self.stdout.write(self.style.SUCCESS(message))
