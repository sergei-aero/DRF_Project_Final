from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    related_habit = serializers.PrimaryKeyRelatedField(
        queryset=Habit.objects.none(),  # временно пустой, будет заполнен в __init__
        required=False,
        allow_null=True
    )

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ['user', 'last_sent']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            # Ограничиваем выбор только привычками текущего пользователя
            self.fields['related_habit'].queryset = Habit.objects.filter(user=request.user)

    def validate(self, data):
        related_habit = data.get('related_habit')
        reward = data.get('reward')
        is_pleasant = data.get('is_pleasant', False)
        execution_time = data.get('execution_time')
        periodicity = data.get('periodicity', 1)

        if related_habit and reward:
            raise serializers.ValidationError('Нельзя одновременно указывать связанную привычку и вознаграждение.')

        if is_pleasant:
            if related_habit or reward:
                raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')

        if related_habit and not related_habit.is_pleasant:
            raise serializers.ValidationError('Связанная привычка должна быть приятной.')

        if execution_time and execution_time > 120:
            raise serializers.ValidationError('Время выполнения не должно превышать 120 секунд.')

        if not (1 <= periodicity <= 7):
            raise serializers.ValidationError('Периодичность должна быть от 1 до 7 дней.')

        return data

