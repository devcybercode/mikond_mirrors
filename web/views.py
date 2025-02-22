from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from .models import mirrors, SocialContact
from django.views.generic import (
    ListView,
)
from .forms import ContactForm
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.http import JsonResponse
 
class index(FormMixin, ListView):
    model = mirrors  
    template_name = "pages/index.html"
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        if 'object_list' not in kwargs:
            kwargs['object_list'] = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['social_contacts'] = SocialContact.objects.all()
        if 'form' not in context:
            context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка успешно отправлена!")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success', 'message': "Ваша заявка успешно отправлена!"})
            else:
                return self.form_valid(form)
        else:
            messages.error(request, "Неверный формат номера телефона или превышен лимит допустимого текста.")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': "Неверный формат номера телефона или превышен лимит допустимого текста."}, status=400)
            else:
                return self.form_invalid(form)