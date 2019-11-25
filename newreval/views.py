from django.shortcuts import render
from .models import Class, UserDetails, Subjects, Sem
from django.contrib import messages


def new_reval_head(request):
    queryset_class = Class.objects.all()
    queryset_sem = Sem.objects.all()
    queryset_subjects = Subjects.objects.all()
    queryset_userdetails = UserDetails.objects.all()
    context = {
        'class': queryset_class,
        'sems': queryset_sem,
        'subjects': queryset_subjects,
        'details': queryset_userdetails
    }

    return render(request, 'newreval/newrevalhead.html', context)


def new_reval(request):
    queryset_class = Class.objects.all()
    queryset_sem = Sem.objects.all()
    queryset_subjects = Subjects.objects.all()
    flag = 1


    if 'CLASS' in request.GET:
        cname = request.GET['CLASS']
        if cname:
            flag = 0
            queryset_subjects = queryset_class.filter(class_id__icontains=cname)
    else:
        pass


    if 'SEM' in request.GET:
        sem = request.GET['SEM']
        if sem:
            flag = 0
            queryset_subjects = queryset_sem.filter(sem_id__exact=sem)
    else:
        pass
    context = {
        'subjects': queryset_subjects

    }

    if flag == 1:
        messages.success(request, f'Enter a value')
        return render(request, 'newreval/newrevalhead.html', {})

    else:
        return render(request, 'newreval/newreval.html', context)
