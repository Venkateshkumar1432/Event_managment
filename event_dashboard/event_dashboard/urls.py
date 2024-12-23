from django.urls import path, include
from rest_framework.routers import DefaultRouter
from management.views import EventViewSet, AttendeeViewSet, TaskViewSet

router = DefaultRouter()
router.register('events', EventViewSet)
router.register('attendees', AttendeeViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]