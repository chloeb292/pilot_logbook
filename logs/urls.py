from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views
from .views import PilotListView
from .views import PilotDetailView

from .views import LogbookListView



urlpatterns = [
    path('add_pilot', views.add_pilot, name='add_pilot'),
    path('pilot/<int:pk>/add_logbook_entry', views.add_logbook_entry, name='add_logbook_entry'),

    path('pilot_display', PilotListView.as_view(), name='pilot-list'),
    path('pilot/<int:pk>/', views.PilotDetailView.as_view(), name='pilot-detail'),

    path('pilot/<int:pk>/edit/', views.pilot_edit, name='pilot_edit'),
    path('logbook_entry_edit/<int:pk>', views.logbook_edit, name='logbook-edit'),



    


    


    
]