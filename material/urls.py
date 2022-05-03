from django.urls import path
from .views import MaterialDetailView, MaterialCreateView, MaterialListView

app_name = 'material'

urlpatterns = [
    path('', MaterialListView.as_view(), name='list'),
    path('add/', MaterialCreateView.as_view(), name='create'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='detail'),
]
