from django.contrib import admin
from .models import Hike, Application

# Регистрация модели Hike в админке
@admin.register(Hike)
class HikeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

# Регистрация модели Application в админке
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'is_canceled')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at', 'is_canceled')