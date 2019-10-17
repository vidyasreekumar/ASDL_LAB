from django.shortcuts import render

def login(request):
    return render(request, 'templates/logreg/login.html', {})

def register(request):
    return render(request, 'logreg/register.html', {})

def dashboard(request):
    return render(request, 'logreg/dashboard.html', {})

def logout(request):
    return render(request, 'logreg/logout.html', {})