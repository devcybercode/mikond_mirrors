from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from .models import mirrors
from django.views.generic import (
    ListView,
)
    
class index(ListView):
    model = mirrors
    template_name = "pages/index.html"