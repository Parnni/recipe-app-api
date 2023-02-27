import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Pyscopg2Error


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        db_up = False

        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (OperationalError, Pyscopg2Error):
                self.stdout.write("Database unavailable, waiting for 5 second...")
                time.sleep(5)

        self.stdout.write(self.style.SUCCESS("Database available."))
