from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_signup, name='register'),
    path('pricing/', views.pricing, name='pricing'),
    path('payment/<str:ref>/<int:amount>', views.payment, name = "payment"),
]
