from django.shortcuts import render, redirect
from .forms import RegisterrForm
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from .models import Registration


# Create your views here.
def welcome(request):
    return render(request, 'Welcome.html')


def register(request):
    if request.method == "POST":
        form = RegisterrForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Listings')
    else:
        form = RegisterrForm()
    return render(request, 'Register.html', {'form': form})


def listings(request):
    obj = Registration.objects.all().order_by("-id")
    return render(request, 'listings.html', {'obj': obj})


def login(request):
    return render(request)


def search(request):
    if 's' in request.GET:
        s=request.GET.get('s')
        plot=Registration.objects.filter(zip__icontains=s)
    else:
        plot = Registration.objects.all()
    return render(request, "Search.html",{'plot':plot})
