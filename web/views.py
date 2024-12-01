from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from .models import mirrors, SocialContact
from django.views.generic import (
    ListView,
)
    
class index(ListView):
    model = mirrors
    template_name = "pages/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social_contacts'] = SocialContact.objects.all()
        return context