from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone']
        widgets = {
            'phone': forms.TextInput(attrs={
                'placeholder': '+998 (__) ___ __ __',
                'id': 'id_phone'
            })
        }
