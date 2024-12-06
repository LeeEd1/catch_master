from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    """
    Handle the display and submission of the contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('thank_you')
        else:
            messages.error(request, 'There was an error with your form, Please try again.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def thank_you(request):
    """
    Render the thank-you page after successful form submission.
    """
    return render(request, 'contact/thankyou.html')