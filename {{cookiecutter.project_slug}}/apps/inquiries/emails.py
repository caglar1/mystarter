import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

def send_inquiry_notification_email(inquiry):
    subject = f"Yeni Teklif Talebi: {inquiry.full_name}"
    message = f"Ad Soyad: {inquiry.full_name}\nE-posta: {inquiry.email}\nTelefon: {inquiry.phone}\nMesaj:\n{inquiry.message}"
    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL], fail_silently=True)
    except Exception as e:
        logger.error(f"Email sending failed: {e}")
