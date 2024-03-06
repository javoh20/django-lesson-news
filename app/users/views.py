from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import  authenticate, login
from django.views.generic import CreateView
from django.http import HttpResponse
from .models import *

# Create your views here.


def UserProfile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'registration/profile.html', context)


# def UserReg(request):
#     if request.method == "POST":
#         user_form = SignupForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(
#                 user_form.cleaned_data['password_1']
#             )
#             new_user.save()
#             context = {
#                 'user_form': user_form,
#             }
#             return render(request, 'account/register_done.html', context)
        
#     else:
#         user_form = SignupForm()
#         context = {
#             'user_form': user_form,
#         }
#         return render(request, 'account/register.html', context)

class UserReg(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')


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