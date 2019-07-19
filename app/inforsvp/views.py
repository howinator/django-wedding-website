from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    context = {}

    return render(request,'inforsvp/index.html', context)

def rsvp(request):

    return HttpResponse('rsvp')
