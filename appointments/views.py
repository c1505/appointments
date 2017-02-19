from django.shortcuts import render
from .forms import AppointmentForm
from django.http import HttpResponse
def index(request):
    return render(request,"appointments/index.html", {})

def create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            return render(request,"appointments/index.html", {})
        else:
            return HttpResponse("Invalid Form")


# will be returning json here i belive
