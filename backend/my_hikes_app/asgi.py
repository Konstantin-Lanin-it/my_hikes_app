import os
from django.core.asgi import get_asgi_application

# Установка переменной окружения для настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_hikes_app.settings')

# Создание ASGI приложения
application = get_asgi_application()