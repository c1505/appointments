from django.shortcuts import render
def index(request):
    return render(request,"appointments/index.html", {})
# will be returning json here i belive
