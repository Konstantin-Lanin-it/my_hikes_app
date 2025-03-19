import os
from celery import Celery

# Установите переменную окружения для настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_hikes_app.settings')  # Замените на ваше название проекта

app = Celery('my_hikes_app')  # Замените на ваше название проекта

# Настройка конфигурации Celery из настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач в приложениях
app.autodiscover_tasks()