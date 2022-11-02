from rest_framework import serializers
from schedule import models


class PairSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pair
        fields = '__all__'


"""
class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Week
        fields = '__all__'

"""
 