from django.contrib import admin
from .models import Pilot
from .models import LogbookEntry


# Register your models here.
admin.site.register(Pilot) 
admin.site.register(LogbookEntry)
