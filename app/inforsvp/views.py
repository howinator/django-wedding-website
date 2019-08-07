from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import RSVPForm
from .models import RSVP


def index(request):

    context = {}

    return render(request,'inforsvp/index.html', context)


def rsvp(request):

    if request.method == 'POST':
        form = RSVPForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            number_attending = form.cleaned_data['number_attending']
            extra_info = form.cleaned_data['extra_info']

            rsvp = RSVP(name=name, email=email, number_attending=number_attending, extra_info=extra_info)

            rsvp.save()
            return HttpResponseRedirect('/thanks/')

    else:
        form = RSVPForm()

    return render(request, 'inforsvp/rsvp.html', {'form': form})


def thanks(request):

    return render(request, 'inforsvp/thanks.html', {})
