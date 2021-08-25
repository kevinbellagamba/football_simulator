from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('name', views.name),
    path('play', views.play),
    path('reset', views.reset),
]
