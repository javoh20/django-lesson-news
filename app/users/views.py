from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import  authenticate, login
from django.views.generic import CreateView
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


def UserProfile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'registration/profile.html', context)


class UserReg(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

@login_required
def UserProfile(request):
    user = request.user
    profile_info = Profile.objects.get(user=user)
    
    context = {
        "user": user,
        "profile_info": profile_info,
    }

    return render(request, 'registration/profile.html', context)

def EditUser(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, 
                                       data=request.POST,
                                       files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        context = {
            "user_form" : user_form,
            "profile_form" : profile_form,
        }

        return redirect('profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        context = {
            "user_form" : user_form,
            "profile_form" : profile_form,
        }

        return render(request, 'user_edit.html', context)
    

@login_required
@user_passes_test(lambda u: u.is_superuser)
def AdminPage(request):
    admin_users = User.objects.filter(is_superuser=True)
    users = User.objects.filter(is_superuser=False)

    context = {
        'admins': admin_users,
        'users': users,
    }

    return render(request, 'admin_page.html', context)
