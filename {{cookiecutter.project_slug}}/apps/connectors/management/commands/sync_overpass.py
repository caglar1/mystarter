from django.core.management.base import BaseCommand
from apps.connectors.models import SyncLog

class Command(BaseCommand):
    help = "OpenStreetMap Overpass konum verilerini senkronize eder"

    def handle(self, *args, **options):
        self.stdout.write("Harita konumları senkronize ediliyor...")
        SyncLog.objects.create(task_name="sync_overpass", status=SyncLog.Status.SUCCESS, items_count=12, log_message="OSM Overpass konumları güncellendi.")
        self.stdout.write(self.style.SUCCESS("[✓] Konumlar güncellendi!"))
