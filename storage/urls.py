from django.urls import path
from . import views

app_name = "storage"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('images/', views.upload_images, name='my_images'),
]
