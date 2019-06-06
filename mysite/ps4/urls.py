from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('event/', views.events, name='events'),
    path('event/<int:event_id>/', views.event, name='event'),
    path('group/', views.group, name='group'),
    # path('create/', views.create, name='create')
]