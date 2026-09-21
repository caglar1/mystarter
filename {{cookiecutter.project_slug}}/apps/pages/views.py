from django.shortcuts import render
from apps.inquiries.forms import InquiryForm

def home_view(request):
    return render(request, 'pages/home.html', {'inquiry_form': InquiryForm()})

def about_view(request):
    return render(request, 'pages/about.html')

def services_view(request):
    return render(request, 'pages/services.html')

def contact_view(request):
    return render(request, 'pages/contact.html', {'form': InquiryForm()})

def ui_kit_view(request):
    return render(request, 'pages/ui_kit.html')
