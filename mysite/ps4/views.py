from django.http import HttpResponse
from .models import Event, Queue
from .model_manager import EventManager, PersonManager
from django.template import loader

events_list = 'events_list'
app = 'app'
app_name = '/ps4'
manager = EventManager()

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def events(request):
    template = loader.get_template('ps4/events.html')
    context = {
        events_list : manager.get_all_events(),
        app : app_name,
    }

    return HttpResponse(template.render(context, request))

def event(request, event_id):
    event = manager.get_event(event_id)

    return HttpResponse(event)

def group(request):
    template = loader.get_template('ps4/group.html')
    context = {
        app : app_name,
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('ps4/main.html')
    context = {
        app : app_name,
    }

    return HttpResponse(template.render(context, request))


# def create(request):
#     PersonManager().create_fake_persons(20)

#     return HttpResponse("created")
