from django.urls import path
from . import views

app_name = 'connectors'

urlpatterns = [
    path('status/', views.sync_status_view, name='sync_status'),
    path('sync-news/', views.sync_news_view, name='sync_news'),
]
