from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Habit

User = get_user_model()


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="testpass")

    def test_create_habit_valid(self):
        habit = Habit.objects.create(
            user=self.user,
            place="Home",
            time="08:00:00",
            action="Morning run",
            is_pleasant=False,
            execution_time=60,
            periodicity=1,
        )
        self.assertEqual(habit.action, "Morning run")
        self.assertTrue(habit.pk)

    def test_execution_time_validation(self):
        with self.assertRaises(Exception):
            Habit.objects.create(
                user=self.user,
                place="Home",
                time="08:00:00",
                action="Too long",
                execution_time=150,
                periodicity=1,
            )


class HabitAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="user@test.com", password="pass")
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        data = {
            "place": "Office",
            "time": "14:00:00",
            "action": "Stretch",
            "is_pleasant": False,
            "execution_time": 30,
            "periodicity": 2,
        }
        response = self.client.post("/api/habits/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)

    def test_public_list(self):
        # создаем публичную привычку и проверяем эндпоинт
        Habit.objects.create(
            user=self.user,
            place="Park",
            time="07:00:00",
            action="Walk",
            is_public=True,
            execution_time=45,
            periodicity=1,
        )
        response = self.client.get("/api/habits/public/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)  # если пагинация включена
