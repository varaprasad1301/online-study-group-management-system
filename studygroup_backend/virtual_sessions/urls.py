from django.urls import path
from .views import virtual_sessions

urlpatterns = [
    path('virtual-sessions/', virtual_sessions, name='virtual_sessions'),
]
 