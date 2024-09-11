from django.shortcuts import render
from .models import Doctor
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
    username = get_user(request).username
    if request.method == 'POST':
        specialization_list = request.POST.getlist('tags')
        doctors = Doctor.objects.filter(category__name__in=specialization_list)
        context = {"doctors": doctors, "username": username}
        return render(request, 'base.html', context)

    doctors = Doctor.objects.all()
    context = {"doctors": doctors, "username": username}
    return render(request, 'home.html', context)
