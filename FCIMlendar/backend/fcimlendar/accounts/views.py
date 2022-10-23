from rest_framework import generics
from accounts import models, serializers


class AccountView(generics.ListCreateAPIView):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountsSerializer
