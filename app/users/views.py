from django.shortcuts import render
from .forms import *
from django.contrib.auth import  authenticate, login
from django.http import HttpResponse

# Create your views here.


def UserProfile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'registration/profile.html', context)