from django.shortcuts import render
from .models import SyncLog

def sync_status_view(request):
    latest_log = SyncLog.objects.first()
    return render(request, 'components/sync_status_badge.html', {'latest_log': latest_log})

def sync_news_view(request):
    latest_log = SyncLog.objects.create(
        task_name="sync_news",
        status=SyncLog.Status.SUCCESS,
        items_count=1,
        log_message="UI üzerinden manuel senkronizasyon tetiklendi."
    )
    return render(request, 'components/sync_status_badge.html', {'latest_log': latest_log})
