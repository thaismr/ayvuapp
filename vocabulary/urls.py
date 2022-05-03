from django.urls import path
from .views import VocabularyCreateView, VocabularyDetailView, VocabularyListView

app_name = 'vocabulary'

urlpatterns = [
    path('', VocabularyListView.as_view(), name='list'),
    path('add/', VocabularyCreateView.as_view(), name='create'),
    path('<int:pk>/', VocabularyDetailView.as_view(), name='detail'),
]
