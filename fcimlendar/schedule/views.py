from rest_framework import generics
from schedule import models, serializers


class PairView(generics.ListCreateAPIView):
    queryset = models.Pair.objects.all()
    serializer_class = serializers.PairSerializer