from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="attendees")

class Task(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.DateField()
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    assigned_attendee = models.ForeignKey(Attendee, on_delete=models.SET_NULL, null=True, related_name="tasks")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tasks")
