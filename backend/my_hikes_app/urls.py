from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ панель
    path('api/v1/public/', include('app.urls')),  # Публичные API URL'ы
    path('api/v1/private/', include('app.urls')),  # Приватные API URL'ы (добавьте в нужное место или создайте отдельный файл)
]