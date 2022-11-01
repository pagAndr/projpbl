from django.urls import path
from timetable import views

urlpatterns = [
    path('', views.LessonView.as_view()),
#    path('test/', views.WeekView.as_view()),
]