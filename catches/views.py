from django.shortcuts import render, redirect
from .models import CatchEntry
from .forms import CatchEntryForm
from django.contrib.auth.decorators import login_required

# Display all catch entries
@login_required
def catch_cam(request):
    entries = CatchEntry.objects.all()
    return render(request, 'catches/catch_cam.html', {'entries': entries})

@login_required
def add_catch(request):
    """
    Adds entry to Catch Cam
    """
    if request.method == 'POST':
        form = CatchEntryForm(request.POST, request.FILES)
        if form.is_valid():
            catch_entry = form.save(commit=False)
            catch_entry.user = request.user
            catch_entry.save()
            messages.success(request, 'Catch successfully added!')
            return redirect('catch_cam')
        else:
            messages.error(request, 'Failed to add catch! Please ensure the form is valid.')
    else:
        form = CatchEntryForm()
    
    template = 'catches/add_catch.html'
    context = {
        'form': form,
    }

    return render(request, template, context)