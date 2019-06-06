from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=250)
    created = models.DateTimeField()

    def __str__(self):
        return self.event_name

class Queue(models.Model):
    name = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    position = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Person(models.Model):
    person_name = models.CharField(max_length=250)

    def __str__(self):
        return self.person_name