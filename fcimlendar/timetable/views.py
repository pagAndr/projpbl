from rest_framework import generics
from timetable import models, serializers


class LessonView(generics.ListCreateAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

