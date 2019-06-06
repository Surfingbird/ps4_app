from django.db import models
from .models import Event, Person
from faker import Faker

fake = Faker()

class EventManager(models.Manager):
    def get_event(self, event_id):
        return Event.objects.filter(id=event_id)
        
    def get_all_events(self):
        return Event.objects.all()

class PersonManager(models.Manager):
    def create_fake_persons(self, count):
        for i in range(count):
            name = fake.name()
            p = Person(person_name=name)
            p.save()

    def get_all_persons(self):
        return Person.objects.all()

