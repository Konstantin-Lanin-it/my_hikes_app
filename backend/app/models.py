from django.db import models

class Hike(models.Model):
    title = models.CharField(max_length=200)  # Название похода
    description = models.TextField()  # Описание похода
    image_url = models.URLField()  # Ссылка на изображение
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания похода

    def __str__(self):
        return self.title  # Удобное представление объекта в админке

class Application(models.Model):
    name = models.CharField(max_length=100)  # Имя заявителя
    email = models.EmailField()  # Email заявителя
    phone = models.CharField(max_length=15)  # Телефон заявителя
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания заявки
    is_canceled = models.BooleanField(default=False)  # Статус отмены заявки
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)  # Связь с моделью Hike

    def __str__(self):
        return f'{self.name} - {self.hike.title}'  # Удобное представление объекта в админке