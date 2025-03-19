from rest_framework import generics
from .models import Hike, Application
from .serializers import HikeSerializer, ApplicationSerializer

class HikeList(generics.ListCreateAPIView):
    """Представление для получения списка походов и создания нового похода."""
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer

class HikeDetail(generics.RetrieveUpdateDestroyAPIView):
    """Представление для получения, обновления или удаления конкретного похода."""
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer

class ApplicationList(generics.ListCreateAPIView):
    """Представление для получения списка заявок и создания новой заявки."""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    """Представление для получения, обновления или удаления конкретной заявки."""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer