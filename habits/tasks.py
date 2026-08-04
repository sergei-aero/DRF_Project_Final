from celery import shared_task
import requests
from django.utils import timezone
from django.conf import settings
from .models import Habit


@shared_task
def send_habit_reminders():
    now = timezone.now()
    # Ищем привычки, у которых время совпадает с текущим (час и минута)
    habits = Habit.objects.filter(
        time__hour=now.hour,
        time__minute=now.minute,
    )

    for habit in habits:
        if not habit.user.telegram_chat_id:
            continue

        # Проверяем периодичность
        if habit.last_sent:
            days_since_last = (now - habit.last_sent).days
            if days_since_last < habit.periodicity:
                continue

        message = (
            f"Напоминание: {habit.action}\n"
            f"Место: {habit.place}\n"
            f"Время: {habit.time.strftime('%H:%M')}\n"
            f"Периодичность: {habit.periodicity} дн."
        )
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": habit.user.telegram_chat_id, "text": message}
        try:
            requests.post(url, data=payload)
            habit.last_sent = timezone.now()
            habit.save(update_fields=["last_sent"])
        except Exception as e:
            print(f"Ошибка отправки уведомления: {e}")
