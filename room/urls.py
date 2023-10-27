from django.urls import path 
from .views import room,home
urlpatterns = [
    path('', home, name='home'),
    path('room/<str:pk>', room, name='room')
]