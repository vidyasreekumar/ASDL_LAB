from django.shortcuts import render

def new_reval(request):
    return render(request, 'templates/newreval/newreval.html', {})