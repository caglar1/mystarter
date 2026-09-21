from django.db import models

class SyncLog(models.Model):
    class Status(models.TextChoices):
        SUCCESS = "success", "Başarılı"
        FAILED = "failed", "Hatalı"
        RUNNING = "running", "Çalışıyor"

    task_name = models.CharField(max_length=100, db_index=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SUCCESS, db_index=True)
    items_count = models.IntegerField(default=0)
    log_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Senkronizasyon Günlüğü"
        verbose_name_plural = "Senkronizasyon Günlükleri"

    def __str__(self):
        return f"[{self.get_status_display()}] {self.task_name} ({self.items_count} öge)"
