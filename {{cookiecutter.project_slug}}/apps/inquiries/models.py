from django.db import models

class Inquiry(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name="E-posta")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Telefon")
    message = models.TextField(verbose_name="Mesaj / Talep")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tarih")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Talep"
        verbose_name_plural = "Talepler"

    def __str__(self):
        return f"{self.full_name} ({self.email})"
