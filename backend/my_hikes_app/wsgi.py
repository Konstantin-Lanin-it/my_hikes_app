import os
from django.core.wsgi import get_wsgi_application

# Установка переменной окружения для настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_hikes_app.settings')

# Создание WSGI приложения
application = get_wsgi_application()