from django.urls import path
from schedule import views

urlpatterns = [
    path('', views.PairView.as_view()),
]