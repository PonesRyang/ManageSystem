from django.urls import path
from rest_framework.routers import DefaultRouter

from port.views import SchedulingViewSet, RoleViewSet, EventTypeViewSet, UserViewSet, UserSchedulingViewSet, \
    EventViewSet, LeaveViewSet

urlpatterns = [

]
router = DefaultRouter()
router.register('Scheduling', SchedulingViewSet)
router.register('Role', RoleViewSet)
router.register('EventType',EventTypeViewSet)
router.register('User',UserViewSet)
router.register('UserScheduling',UserSchedulingViewSet)
router.register('Event',EventViewSet)
router.register('Leave',LeaveViewSet)
urlpatterns += router.urls
