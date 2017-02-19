from django.shortcuts import render
from .forms import AppointmentForm
from django.http import HttpResponse
import pdb
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


# will be returning json here i belive
