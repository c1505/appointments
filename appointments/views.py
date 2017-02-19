from django.shortcuts import render
from .forms import AppointmentForm
from django.http import HttpResponse
import pdb
from appointments.models import Appointment
import json
from django.http import JsonResponse
from django.core import serializers
def index(request):
    return render(request,"appointments/index.html", {})

def create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        # pdb.set_trace()
        # datetime = request.POST['datetime']
        # description = request.POST['description']
        if form.is_valid():
            return render(request,"appointments/index.html", {})
        else:
            return HttpResponse("Invalid Form")

def app(request):
    appointments = Appointment.objects.all().values('datetime', 'description')
    response = JsonResponse(dict(appointments=list(appointments)))
    return response
