from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('remover_dispositivo/<int:dispositivo_id>/', views.remover_dispositivo, name="remover_dispositivo")
]
