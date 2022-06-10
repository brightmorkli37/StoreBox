from django.urls import path
from . import views

app_name = "storage"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('images/', views.upload_images, name='my_images'),
    path('audio_files/', views.upload_audio, name='my_audios'),
    path('videos/', views.upload_videos, name='my_videos'),
    path('documents/', views.upload_files, name='my_files'),
]
