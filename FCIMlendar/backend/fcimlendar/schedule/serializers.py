from rest_framework import serializers
from schedule import models


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Week
        fields = '__all__'
#        exclude = ['occupant']
 