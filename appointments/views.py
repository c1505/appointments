from django.shortcuts import render
from django.shortcuts import redirect
from .forms import AppointmentForm
from django.http import HttpResponse
import pdb
from appointments.models import Appointment
import json
from django.http import JsonResponse
from django.core import serializers
def index(request):
    form = AppointmentForm()
    return render(request,"appointments/index.html", {'form': form})

def create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        # pdb.set_trace()
        # datetime = request.POST['datetime']
        # description = request.POST['description']
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return HttpResponse("Invalid Form")

def app(request):
    params = request.GET['params']
    if params:
        appointments = Appointment.objects.filter(description=params)
    else:
        appointments = Appointment.objects.all()
    appointments = appointments.values('datetime', 'description')
    response = JsonResponse(dict(appointments=list(appointments)))
    return response
