# Трекер полезных привычек

Проект представляет собой бэкенд-часть SPA-приложения для отслеживания полезных привычек, разработанный на Django REST Framework.

## Функциональность

- Регистрация и аутентификация пользователей (JWT).
- CRUD привычек с валидацией.
- Публичные привычки (доступны для просмотра всем авторизованным пользователям).
- Пагинация (5 привычек на страницу).
- Периодические напоминания в Telegram (Celery + Redis).
- Документация API (Swagger/ReDoc).

## Технологии

- Python 3.12
- Django 5+
- Django REST Framework
- PostgreSQL
- Celery + Redis
- django-celery-beat
- drf-yasg (Swagger)
- django-cors-headers

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone git@github.com:sergei-aero/DRF_Project_Final.git
cd DRF_Project_Final