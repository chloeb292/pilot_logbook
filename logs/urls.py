from django.urls import path

from . import views
from .views import PilotListView


urlpatterns = [
    path('add_pilot', views.add_pilot, name='add_pilot'),
    path('pilot_list', PilotListView.as_view(), name='pilot-list'),

    
]