from django.urls import path
from timetable import views

urlpatterns = [
    path('lesson/', views.LessonView.as_view()),
    path('prof/', views.ProfView.as_view()),
    path('group/', views.GroupView.as_view()),
    path('room/', views.RoomView.as_view()),
#    path('test/', views.WeekView.as_view()),
]