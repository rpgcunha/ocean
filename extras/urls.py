from django.urls import path
from . import views

urlpatterns = [
    path('social-media/', views.media, name='media'),
]