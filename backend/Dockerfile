# Используем официальный образ Python в качестве базового образа
FROM python:3.10-slim

# Установка переменной окружения для предотвращения создания .pyc файлов
ENV PYTHONDONTWRITEBYTECODE 1

# Установка переменной окружения для установки пакетов в директории, доступной для всех пользователей
ENV PYTHONUNBUFFERED 1

# Обновление пакетов и установка необходимых зависимостей
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Создание рабочей директории
WORKDIR /app

# Копирование файлов requirements.txt в рабочую директорию
COPY requirements.txt ./

# Установка зависимостей из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего кода приложения в контейнер
COPY . .

# Выполнение миграций и создание суперпользователя
RUN python manage.py makemigrations
RUN python manage.py migrate

# Порт для доступа к приложению
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_hikes_app.wsgi:application"]