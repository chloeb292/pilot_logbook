
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Pilot
from .models import LogbookEntry

from .forms import PilotForm
from .forms import LogbookEntryForm



# Create your views here.

def add_pilot(request):
    if request.method == "POST":
        pilot_form = PilotForm(request.POST)
        print(pilot_form)
        if pilot_form.is_valid():
            pilot = pilot_form.save(commit=False)
            pilot.save()
            return redirect('pilot-list')
    else:
        pilot_form = PilotForm()
    return render(request, 'logs/add_pilot.html', {'pilot_form': pilot_form})

def pilot_edit(request, pk):
    pilot = get_object_or_404(Pilot, pk=pk)
    if request.method == "POST":
        pilot_form = PilotForm(request.POST, instance=pilot)
        if pilot_form.is_valid():
            post = pilot_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('pilot-list')
    else:
        pilot_form = PilotForm(instance=pilot)
    return render(request, 'logs/add_pilot.html', {'pilot_form': pilot_form})

def logbook_edit(request, pk):
    entry = get_object_or_404(LogbookEntry, pk=pk)
    if request.method == "POST":
        logbook_entry_form = LogbookEntryForm(request.POST, instance=entry)
        if logbook_entry_form.is_valid():
            post = logbook_entry_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('pilot-list')
    else:
        logbook_entry_form = LogbookEntryForm(instance=entry)
    return render(request, 'logs/add_logbook_entry.html', {'logbook_entry_form': logbook_entry_form})




#FIGURING OUT logbook entries

def add_logbook_entry(request, pk):
    if request.method == "POST":
        logbook_entry_form = LogbookEntryForm(request.POST)
        print(logbook_entry_form)
        if logbook_entry_form.is_valid():
            logbook_entry = logbook_entry_form.save(commit=False)
            logbook_entry.save()
            return redirect('pilot-list')
    else:
        logbook_entry_form = LogbookEntryForm
    return render(request, 'logs/add_logbook_entry.html', {'logbook_entry_form': logbook_entry_form})






class PilotListView(ListView):
    model = Pilot

    def pilot_display(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PilotDetailView(DetailView):
    model = Pilot 
    
    def get(self, request, *args, **kwargs):
        pilot = get_object_or_404(Pilot, pk=kwargs['pk'])
        #pilot_logs = get_object_or_404(LogbookEntry, pk=kwargs['pk'])
        lbe = LogbookEntry.objects.filter(pilot_id=kwargs['pk'])
        context = {'pilot': pilot, 'pilot_logs': lbe}
        return render(request, 'logs/pilot_detail.html', context)
     
class LogbookListView(ListView):
    model = LogbookEntry

    def logbook_entry_display(self, request, *args, **kwargs):
        logbook_entry = get_object_or_404(LogbookEntry, pk=kwargs['pk'])
        context = {'logbook_entry': logbook_entry} 
        return render(request, 'logs/logbookentry_list.html', context)

