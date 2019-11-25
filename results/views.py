from django.shortcuts import render

# Create your views here.
def result(request):
    return render(request=request, template_name="main/result.html", context={})

