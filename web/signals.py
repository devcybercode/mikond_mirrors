# signals.py
import requests
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact

@receiver(post_save, sender=Contact)
def send_contact_to_telegram(sender, instance, created, **kwargs):
    if created:
        message = (
            f"Новая заявка:\n"
            f"Имя: {instance.name}\n"
            f"Телефон: {instance.phone}\n"
        )
        if instance.model:
            message += f"Модель зеркало: {instance.model.title}\n"
        else:
            message += "Модель зеркало: Пользователь не выбрал\n"
        
        bot_token = settings.MIKOND_TELEGRAM_BOT_TOKEN
        chat_id = settings.MIKOND_TELEGRAM_CHAT_ID
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()  
        except Exception as e:
            print("Не получилось отправить сообщение:", e)