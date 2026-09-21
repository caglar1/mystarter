from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['full_name', 'email', 'phone', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Ahmet Yılmaz'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ahmet@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '0555 123 45 67'}),
            'message': forms.Textarea(attrs={'placeholder': 'Projeniz hakkında kısaca bilgi verin...', 'rows': 4}),
        }
