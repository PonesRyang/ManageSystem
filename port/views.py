from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from port.models import Scheduling, Role, EventType, User, UserScheduling, Event, Leave
from port.serializers import SchedulingSerializer, RoleSerializer, EventTypeSerializer, UserSerializer, \
    UserSchedulingSerializer, EventSerializer, LeaveSerializer


class SchedulingViewSet(ModelViewSet):
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer
    pagination_class = None


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    pagination_class = None


class EventTypeViewSet(ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    pagination_class = None


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSchedulingViewSet(ModelViewSet):
    queryset = UserScheduling.objects.all()
    serializer_class = UserSchedulingSerializer
    pagination_class = None


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class LeaveViewSet(ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
