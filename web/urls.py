from django.urls import path, include, reverse_lazy
from .views import (
    index,
)

# from django.views.i18n import set_language

app_name = "main"

urlpatterns = [
    path('', index.as_view(), name="index"),
]