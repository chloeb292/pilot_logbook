from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views
from .views import PilotListView


urlpatterns = [
    path('add_pilot', views.add_pilot, name='add_pilot'),
    path('pilot_display', PilotListView.as_view(), name='pilot-list'),

    
]