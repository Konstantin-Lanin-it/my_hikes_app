from rest_framework import serializers
from .models import Hike, Application

class HikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hike
        fields = ['id', 'title', 'description', 'image_url', 'created_at']  # Укажите поля модели, которые вы хотите сериализовать

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'name', 'email', 'phone', 'created_at', 'is_canceled', 'hike']  # Укажите поля модели, которые вы хотите сериализовать