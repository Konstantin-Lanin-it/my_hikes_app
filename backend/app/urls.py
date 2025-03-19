from django.urls import path
from .views import HikeList, HikeDetail, ApplicationList, ApplicationDetail

urlpatterns = [
    path('hikes/', HikeList.as_view(), name='hike-list'),  # Список походов
    path('hikes/<int:pk>/', HikeDetail.as_view(), name='hike-detail'),  # Детали конкретного похода
    path('applications/', ApplicationList.as_view(), name='application-list'),  # Список заявок
    path('applications/<int:pk>/', ApplicationDetail.as_view(), name='application-detail'),  # Детали конкретной заявки
]