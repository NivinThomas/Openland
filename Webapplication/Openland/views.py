from django.shortcuts import render, redirect
from .forms import RegisterrForm, LoginForm,NewusrForm
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from .models import Registration, Login,New
from django.contrib.auth import login, authenticate


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


def usr_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Listings')

        else:
            messages.success(request,"Unable to login please try again !")
            redirect('Login')
    else:
        form = NewusrForm
    return render(request, 'Login.html', {'form': form})


def new(request):
    if request.method == "POST":
        form = NewusrForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("Listings")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewusrForm
    return render(request,'Newaccount.html',{'form':form})


def search(request):
    if 's' in request.GET:
        s = request.GET.get('s')
        plot = Registration.objects.filter(zip__icontains=s)
    else:
        plot = Registration.objects.all()
    return render(request, "Search.html", {'plot': plot})
