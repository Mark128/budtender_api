from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EventSerializer
from .models import Event


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-event_datetime')
    serializer_class = EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')

