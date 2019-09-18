import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from .forms import RSVPForm
from .models import RSVP


def index(request):

    context = {}

    raise Exception('lol')

    return render(request,'inforsvp/index.html', context)


def rsvp(request):

    if request.method == 'POST':
        form = RSVPForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            number_attending = form.cleaned_data['number_attending']
            extra_info = form.cleaned_data['extra_info']

            g_captcha_rsp = form.data['g-recaptcha-response']
            capthca_secret = settings.CAPTCHA_SECRET

            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data = {'secret': capthca_secret, 'response': g_captcha_rsp}
            )

            captcha_check_resp = r.json()

            if not captcha_check_resp['success']:
                return HttpResponseRedirect('/need_help/')
            else:
                rsvp = RSVP(name=name, email=email, number_attending=number_attending, extra_info=extra_info)

                rsvp.save()
                return HttpResponseRedirect('/thanks/')
    else:
        form = RSVPForm()

        return render(request, 'inforsvp/rsvp.html', {'form': form})

def need_help(request):
    return render(request, 'inforsvp/need_help.html', {})


def thanks(request):

    return render(request, 'inforsvp/thanks.html', {})
