"""
Django comand to wait for database to be available.
"""
import time
from psycopg2 import OperationalError as Psycopg20pError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        db_up = False
        while db_up is False:
            try:
                self.check(database=['default'])
                db_up=True
            except:
                self.stdout.write(self.style.SUCCESS('Database available!'))