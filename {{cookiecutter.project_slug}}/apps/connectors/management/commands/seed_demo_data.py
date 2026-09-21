from django.core.management.base import BaseCommand
from apps.inquiries.models import Inquiry
from apps.connectors.models import SyncLog

class Command(BaseCommand):
    help = "AI ve test süreçleri için veritabanına anında örnek veriler ekler"

    def handle(self, *args, **options):
        # 1. Örnek Talepler
        inquiries_data = [
            {"full_name": "Ahmet Yılmaz", "email": "ahmet@example.com", "phone": "0555 111 22 33", "message": "Kurumsal web tasarım ve yazılım projesi için teklif almak istiyoruz."},
            {"full_name": "Zeynep Kaya", "email": "zeynep@example.com", "phone": "0532 444 55 66", "message": "E-ihracat altyapısı ve entegrasyon süreçleri hakkında bilgi talep ediyorum."},
            {"full_name": "Mehmet Demir", "email": "mehmet@example.com", "phone": "0544 777 88 99", "message": "Mobil uyumlu modern iş uygulaması geliştirme hizmeti rica ediyoruz."},
        ]

        created_inquiries = 0
        for item in inquiries_data:
            _, created = Inquiry.objects.get_or_create(email=item["email"], defaults=item)
            if created:
                created_inquiries += 1

        # 2. Örnek Senkronizasyon Logları
        SyncLog.objects.get_or_create(
            task_name="system_init",
            defaults={"status": SyncLog.Status.SUCCESS, "items_count": created_inquiries, "log_message": "Sistem ilk kurulum ve demo veri yüklemesi tamamlandı."}
        )

        self.stdout.write(self.style.SUCCESS(f"[✓] {created_inquiries} adet örnek talep ve senkronizasyon kaydı başarıyla oluşturuldu!"))
