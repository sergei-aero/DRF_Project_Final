<<<<<<< HEAD
# DRF Project Final — Платформа автоматических рассылок

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/DRF-3.17-a30000?logo=django&logoColor=white)](https://django-rest-framework.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?logo=postgresql&logoColor=white)](https://postgresql.org)
[![Celery](https://img.shields.io/badge/Celery-5.6-37814A?logo=celery&logoColor=white)](https://docs.celeryq.dev)
[![Redis](https://img.shields.io/badge/Redis-8.0-DC382D?logo=redis&logoColor=white)](https://redis.io)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📖 О проекте

**DRF Project Final** — это бэкенд платформы для автоматических рассылок, разработанный на Django REST Framework. Проект обеспечивает управление пользователями, создание и отправку email-уведомлений подписчикам об обновлениях курсов, а также выполнение периодических задач (например, блокировка неактивных пользователей).

Ключевая особенность — **асинхронная обработка задач** с использованием Celery и Redis, что гарантирует мгновенную доставку уведомлений и фоновое выполнение регламентных операций.

Проект полностью **контейнеризирован** с использованием Docker и может быть развёрнут на удалённом сервере через **GitHub Actions CI/CD**.

---

## 🔥 Основные возможности

- 👤 **Кастомная модель пользователя** — авторизация по email.
- 📨 **Управление подписками** — пользователи могут подписываться на курсы и получать уведомления.
- ⏰ **Периодические задачи** — автоматическая блокировка неактивных пользователей (не заходили > 30 дней).
- 🐳 **Docker-контейнеризация** — все сервисы (Django, PostgreSQL, Redis, Celery, Nginx) запускаются одной командой.
- 🤖 **CI/CD** — автоматическое тестирование, линтинг, сборка и деплой на сервер через GitHub Actions.
- 📄 **Документация API** — интерактивная документация через Swagger UI и ReDoc.
- 🔒 **Безопасность** — CORS настроен, переменные окружения вынесены в `.env`.

---

## 🛠 Технологический стек

| Компонент | Технология |
|-----------|------------|
| **Язык** | Python 3.12 |
| **Фреймворк** | Django 6.0 |
| **API** | Django REST Framework 3.17 |
| **База данных** | PostgreSQL 15 |
| **Брокер задач** | Redis 8.0 |
| **Асинхронные задачи** | Celery 5.6 |
| **Планировщик** | Celery Beat + django-celery-beat |
| **Аутентификация** | JWT (SimpleJWT) |
| **Документация** | drf-yasg (Swagger/ReDoc) |
| **CORS** | django-cors-headers |
| **Управление зависимостями** | Poetry |
| **Контейнеризация** | Docker / Docker Compose |
| **CI/CD** | GitHub Actions |

---

## 🚀 Быстрый старт (локально)

### Требования

- Python 3.12 или выше
- Poetry
- PostgreSQL 15 (локально или через Docker)
- Redis 8.0 (локально или через Docker)
=======
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
>>>>>>> master

### 1. Клонирование репозитория

```bash
<<<<<<< HEAD
git clone https://github.com/sergei-aero/DRF_Project_Final.git
cd DRF_Project_Final
git checkout DRF_2XFinal   # или ваша рабочая ветка
2. Установка зависимостей через Poetry
bash
poetry install
3. Настройка переменных окружения
Скопируйте .env.template в .env и заполните его:

bash
cp .env.template .env
Пример содержимого .env:

ini
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=drf_project_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
4. Создание базы данных
bash
psql -U postgres -c "CREATE DATABASE drf_project_db;"
5. Применение миграций
bash
poetry run python manage.py migrate
6. Создание суперпользователя
bash
poetry run python manage.py createsuperuser
7. Запуск Redis
bash
# macOS (Homebrew)
brew services start redis

# Linux
sudo systemctl start redis

# или вручную
redis-server
8. Запуск Celery Worker и Beat
В двух отдельных терминалах:

bash
# Worker
poetry run celery -A config worker --loglevel=info

# Beat (планировщик)
poetry run celery -A config beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
9. Запуск сервера разработки
bash
poetry run python manage.py runserver
Приложение будет доступно по адресу: http://localhost:8000

🐳 Запуск через Docker Compose
Для локального запуска всех сервисов (Django, PostgreSQL, Redis, Celery, Nginx) одной командой:

bash
docker compose -f docker-compose.prod.yml up -d --build
После запуска выполните миграции и создайте суперпользователя:

bash
docker compose -f docker-compose.prod.yml exec web poetry run python manage.py migrate
docker compose -f docker-compose.prod.yml exec web poetry run python manage.py createsuperuser
Приложение будет доступно по адресу: http://localhost:8080

Остановка:

bash
docker compose -f docker-compose.prod.yml down
Просмотр логов:

bash
docker compose -f docker-compose.prod.yml logs -f
🤖 CI/CD с GitHub Actions
В репозитории настроен автоматический пайплайн (.github/workflows/deploy.yml), который выполняется при пуше в ветку DRF_2XFinal.

Этапы пайплайна:
Линтинг (lint) — проверка кода с помощью flake8.

Тесты (test) — запуск тестов Django с PostgreSQL и Redis в качестве сервисов.

Сборка (build) — проверка сборки Docker-образов.

Деплой (deploy) — автоматический деплой на удалённый сервер (Yandex Cloud) через SSH.

Секреты GitHub
Для работы деплоя необходимо добавить следующие секреты в репозиторий (Settings → Secrets and variables → Actions):

Secret	Описание
SERVER_HOST	Публичный IP-адрес вашего сервера
SERVER_USER	Имя пользователя на сервере (обычно ubuntu)
SSH_PRIVATE_KEY	Приватный SSH-ключ для подключения к серверу
☁️ Деплой на удалённый сервер (Yandex Cloud)
1. Создание ВМ
ОС: Ubuntu 22.04 LTS или 24.04 LTS.

Ресурсы: 2 vCPU, 2 ГБ RAM, 20 ГБ SSD.

Публичный IP: автоматически.

SSH-ключ: добавьте свой публичный ключ.

2. Установка Docker и Docker Compose на сервере
bash
sudo apt update
sudo apt install -y docker.io docker-compose-v2
sudo usermod -aG docker ubuntu
Выйдите и зайдите заново для применения прав.

3. Клонирование репозитория на сервер
bash
cd /home/ubuntu
git clone https://github.com/sergei-aero/DRF_Project_Final.git
cd DRF_Project_Final
git checkout DRF_2XFinal
4. Настройка .env на сервере
bash
cp .env.template .env
nano .env
Заполните переменные:

DEBUG=False

ALLOWED_HOSTS=IP_вашего_сервера,localhost

DB_HOST=db (имя сервиса в Docker)

Все остальные переменные (секретный ключ, пароли БД, Redis)

5. Открытие порта 8080 в группе безопасности
В Yandex Cloud добавьте правило для входящего трафика:

Протокол: TCP

Порт: 8080

Источник: 0.0.0.0/0

6. Запуск контейнеров на сервере вручную (для первого раза)
bash
docker compose -f docker-compose.prod.yml up -d --build
7. Проверка работоспособности
Откройте в браузере: http://<IP_сервера>:8080

📚 Документация API
После запуска сервера документация доступна по адресам:

Swagger UI: /docs/swagger/

ReDoc: /docs/redoc/

🧪 Тестирование
Запуск всех тестов:

bash
poetry run python manage.py test
Запуск тестов с покрытием:

bash
poetry run coverage run manage.py test
poetry run coverage report -m
📁 Структура проекта
text
DRF_Project_Final/
├── config/                 # Настройки проекта
│   ├── settings.py
│   ├── urls.py
│   └── celery.py
├── users/                  # Приложение пользователей
├── materials/              # Приложение материалов (курсы/уроки)
├── .env                    # Переменные окружения (не в репозитории)
├── .env.template           # Шаблон переменных окружения
├── Dockerfile              # Сборка Docker-образа
├── docker-compose.prod.yml # Оркестрация для продакшена
├── nginx.conf              # Конфигурация Nginx
├── .github/workflows/      # GitHub Actions
│   └── deploy.yml
├── pyproject.toml          # Зависимости Poetry
└── README.md               # Этот файл
🤝 Вклад в проект
Создайте форк репозитория.

Создайте ветку для вашей фичи: git checkout -b feature/amazing-feature.

Закоммитьте изменения: git commit -m 'Add amazing feature'.

Запушьте ветку: git push origin feature/amazing-feature.

Откройте Pull Request.

📝 Лицензия
Распространяется под лицензией MIT. Подробнее см. файл LICENSE.

📧 Контакты
Автор: Сергей Павлов
Email: pavlov.aero@gmail.com
GitHub: sergei-aero

⭐ Если проект оказался полезным, поставьте звезду на GitHub!
=======
git clone git@github.com:sergei-aero/DRF_Project_Final.git
cd DRF_Project_Final
>>>>>>> master
