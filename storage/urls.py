from django.urls import path
from . import views

app_name = "storage"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('images/', views.upload_images, name='my_images'),
    path('audio_files/', views.upload_audio, name='my_audios'),
    path('videos/', views.upload_videos, name='my_videos'),
    path('documents/', views.upload_files, name='my_files'),

    path('delete_image/<int:pk>/', views.delete_image, name='delete_image'),
    path('delete_video/<int:pk>/', views.delete_video, name='delete_video'),
    path('get_image/<int:pk>/', views.get_image, name='get_image'),
]
