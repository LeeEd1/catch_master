from django.shortcuts import render
from .models import CatchEntry

# Display all catch entries
def catch_cam(request):
    return render(request, 'catches/catch_cam.html')

def add_catch(request):
    return render(request, 'catches/add_catch.html')