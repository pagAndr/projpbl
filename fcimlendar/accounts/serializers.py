from rest_framework import serializers
from accounts import models


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        exclude = ['is_admin']
 