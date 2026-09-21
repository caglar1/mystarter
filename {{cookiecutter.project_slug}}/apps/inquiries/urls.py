from django.urls import path
from . import views

app_name = 'inquiries'

urlpatterns = [
    path('submit/', views.submit_inquiry_view, name='submit'),
]
