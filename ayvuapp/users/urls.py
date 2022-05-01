from django.urls import path
from .views import UserProfileCreate, UserProfileDetail

app_name = 'profile'

urlpatterns = [
    path('add/', UserProfileCreate.as_view(), name='create'),
    path('<slug:username>/', UserProfileDetail.as_view(), name='detail'),
]
