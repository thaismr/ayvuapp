from django.urls import path
from .views import MaterialDetailView, MaterialCreateView

app_name = 'material'

urlpatterns = [
    path('add/', MaterialCreateView.as_view(), name='create'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='detail'),
]
