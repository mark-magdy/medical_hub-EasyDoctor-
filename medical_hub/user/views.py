from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisteration
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def done(request):
    return render(request, 'done.html')


def landing(request):
    if request.method == 'POST' and request.POST.get("enter") == "signup":
        form = UserRegisteration(request.POST)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data.get('is_staff_field') == 's':
                user.is_staff = True
            user.save()
            auth_login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Your Account has been created')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    elif request.method == 'POST' and request.POST.get("enter") == "login":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    form = UserRegisteration()
    context = {'form': form}
    return render(request, 'landing.html', context)


def mylogout(request):
    request.session.flush()
    return redirect('landing')
