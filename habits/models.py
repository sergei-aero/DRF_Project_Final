from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name='Пользователь'
    )
    place = models.CharField(max_length=255, verbose_name='Место')
    time = models.TimeField(verbose_name='Время выполнения')
    action = models.CharField(max_length=255, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная привычка')
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Связанная привычка'
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Периодичность (дни)',
        help_text='От 1 до 7 дней'
    )
    reward = models.CharField(max_length=255, blank=True, null=True, verbose_name='Вознаграждение')
    execution_time = models.PositiveSmallIntegerField(
        verbose_name='Время на выполнение (сек)',
        help_text='Не более 120 секунд'
    )
    is_public = models.BooleanField(default=False, verbose_name='Публичная')
    last_sent = models.DateTimeField(null=True, blank=True, verbose_name='Последнее уведомление')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['-id']

    def clean(self):
        # 1. Нельзя одновременно выбрать связанную привычку и вознаграждение
        if self.related_habit and self.reward:
            raise ValidationError('Нельзя одновременно указывать связанную привычку и вознаграждение.')

        # 2. Время выполнения не больше 120 секунд
        if self.execution_time > 120:
            raise ValidationError('Время выполнения не должно превышать 120 секунд.')

        # 3. У приятной привычки не может быть вознаграждения или связанной привычки
        if self.is_pleasant:
            if self.related_habit or self.reward:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')

        # 4. Связанная привычка должна быть приятной
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError('Связанная привычка должна быть приятной.')

        # 5. Периодичность от 1 до 7 дней
        if not (1 <= self.periodicity <= 7):
            raise ValidationError('Периодичность должна быть от 1 до 7 дней.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.action} в {self.time} в {self.place}"
