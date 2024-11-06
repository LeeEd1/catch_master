from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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

@login_required
def edit_catch(request, catch_id):
    """
    Edit an existing CatchEntry
    """
    catch_entry = get_object_or_404(CatchEntry, id=catch_id)

    if catch_entry.user != request.user and not request.user.is_superuser:
        messages.error(request, "Sorry, only the owner and superuser can do this.")
        return redirect('catch_cam')

    if request.method == 'POST':
        form = CatchEntryForm(request.POST, request.FILES, instance=catch_entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Catch successfully updated!')
            return redirect('catch_cam')
        else:
            messages.error(request, 'Failed to update catch! Please ensure the form is valid.')
    else:
        form = CatchEntryForm(instance=catch_entry)
    
    template = 'catches/edit_catch.html'
    context = {
        'form': form,
        'catch': catch_entry
    }

    return render(request, template, context)

@login_required
def delete_catch(request, catch_id):
    """
    Deletes an existing CatchEntry
    """
    catch_entry = get_object_or_404(CatchEntry, id=catch_id)

    if catch_entry.user != request.user and not request.user.is_superuser:
        messages.error(request, "Sorry, only the owner and superuser can do this.")
        return redirect('catch_cam')

    catch_entry.delete()
    messages.success(request, 'Catch successfully deleted!')
    return redirect('catch_cam')