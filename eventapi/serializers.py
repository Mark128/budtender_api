# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('user', 'strain', 'event_info', 'event_datetime', 'last_update')
