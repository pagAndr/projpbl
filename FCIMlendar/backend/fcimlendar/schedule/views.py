from rest_framework import generics
from schedule import models, serializers


class ScheduleView(generics.ListCreateAPIView):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
