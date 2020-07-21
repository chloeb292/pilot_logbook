# users/urls.py
from django.urls import path
from .views import SignUpView
from . import views


urlpatterns = [
    path('', views.main, name='main_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
    #path('add_pilot', views.add_pilot, name='add_pilot'),
]