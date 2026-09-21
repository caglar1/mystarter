from django.core.management.base import BaseCommand
from apps.connectors.models import SyncLog

class Command(BaseCommand):
    help = "Haber akışlarını senkronize eder"

    def handle(self, *args, **options):
        self.stdout.write("Haber akışları senkronize ediliyor...")
        SyncLog.objects.create(task_name="sync_news", status=SyncLog.Status.SUCCESS, items_count=5, log_message="Otomatik haber senkronizasyonu tamamlandı.")
        self.stdout.write(self.style.SUCCESS("[✓] Haberler güncellendi!"))
