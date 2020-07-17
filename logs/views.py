
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Pilot
from .forms import PilotForm



# Create your views here.

def index(request):
    return HttpResponse("output")

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
        context = {'pilot': pilot}
        return render(request, 'logs/pilot_detail.html', context)



