from celery import shared_task
from django.utils import timezone
from django.conf import settings
from .models import Habit
import requests

@shared_task
def send_habit_reminders():
    now = timezone.now()
    today = now.date()
    habits = Habit.objects.filter(
        time__hour=now.hour,
        time__minute=now.minute,
    ).exclude(last_sent__date=today)

    for habit in habits:
        if habit.user.telegram_chat_id:
            message = (
                f"Напоминание: {habit.action}\n"
                f"Место: {habit.place}\n"
                f"Время: {habit.time.strftime('%H:%M')}\n"
                f"Периодичность: {habit.periodicity} дн."
            )
            url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {
                'chat_id': habit.user.telegram_chat_id,
                'text': message
            }
            try:
                requests.post(url, data=payload)
                habit.last_sent = timezone.now()
                habit.save(update_fields=['last_sent'])
            except Exception as e:
                print(f"Ошибка отправки уведомления: {e}")

