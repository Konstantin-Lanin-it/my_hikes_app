from django.apps import AppConfig

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Авто увеличиваемый ID
    name = 'app'  # Название вашего приложения
    verbose_name = 'Hikes Application'  # Человекочитаемое имя приложения для панели администратора