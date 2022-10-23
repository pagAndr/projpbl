from django.contrib import admin
from django.urls import path

from administration import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),

]