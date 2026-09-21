from django.shortcuts import render
from django.contrib import messages
from honeypot.decorators import check_honeypot
from .forms import InquiryForm
from .emails import send_inquiry_notification_email

@check_honeypot
def submit_inquiry_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            send_inquiry_notification_email(inquiry)
            messages.success(request, "Talebiniz başarıyla alındı! En kısa sürede sizinle iletişime geçeceğiz.")
            if request.htmx:
                return render(request, 'partials/inquiry_success.html', {'inquiry': inquiry})
            return render(request, 'pages/contact.html', {'form': InquiryForm(), 'success': True})
        else:
            messages.error(request, "Lütfen formdaki hataları kontrol ediniz.")
    else:
        form = InquiryForm()

    context = {'form': form}
    if request.htmx:
        return render(request, 'partials/inquiry_form.html', context)
    return render(request, 'pages/contact.html', context)
