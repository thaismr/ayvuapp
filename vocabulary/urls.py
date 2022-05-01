from django.urls import path
from .views import VocabularyCreateView, VocabularyDetailView

app_name = 'vocabulary'

urlpatterns = [
    path('add/', VocabularyCreateView.as_view(), name='create'),
    path('<int:pk>/', VocabularyDetailView.as_view(), name='detail'),
]
