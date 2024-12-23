from rest_framework import serializers
from .models import Event, Attendee, Task

class EventSerializer(serializers.ModelSerializer):
    attendees = serializers.StringRelatedField(many=True, read_only=True)  # Optional: Display attendees for an event

    class Meta:
        model = Event
        fields = '__all__'

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
