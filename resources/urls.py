from django.urls import path
from .views import ResourceDetailView, ResourceCreateView, ResourceListView

app_name = 'resource'

urlpatterns = [
    path('', ResourceListView.as_view(), name='list'),
    path('add/', ResourceCreateView.as_view(), name='create'),
    path('<int:pk>/', ResourceDetailView.as_view(), name='detail'),
]
