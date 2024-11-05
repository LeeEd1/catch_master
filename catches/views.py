from django.shortcuts import render, redirect
from .models import CatchEntry
from .forms import CatchEntryForm

# Display all catch entries
def catch_cam(request):
    entries = CatchEntry.objects.all()
    return render(request, 'catches/catch_cam.html', {'entries': entries})

def add_catch(request):
    if request.method == 'POST':
        form = CatchEntryForm(request.POST, request.FILES)
        if form.is_valid():
            catch_entry = form.save(commit=False)
            catch_entry.user = request.user
            catch_entry.save()
            return redirect('catch_cam')
    else:
        form = CatchEntryForm()
    
    return render(request, 'catches/add_catch.html', {'form': form})