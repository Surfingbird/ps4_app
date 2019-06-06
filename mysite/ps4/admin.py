from django.contrib import admin

from .models import Event, Queue, Person

admin.site.register(Event)
admin.site.register(Queue)
admin.site.register(Person)


