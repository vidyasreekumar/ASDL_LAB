from django.shortcuts import render
from .models import Class, UserDetails, Subjects, Sem, Reval2
from django.contrib import messages
from django.contrib.auth.models import User


def new_reval_head(request):

    queryset_class = Class.objects.all()
    queryset_sem = Sem.objects.all()
    queryset_subjects = Subjects.objects.all()
    queryset_userdetails = UserDetails.objects.all()


    if request.POST:
        us=request.POST.get('username')
        queryset_userdetails = queryset_subjects.filter(ktu_id=us)
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
    queryset_userdetails = UserDetails.objects.all()
    flag = 1

    print(request.GET)
    if 'SEM' and 'CLASS' in request.GET:
        flag = 0
        sem = request.GET.getlist('SEM', None)[0]
        cname = request.GET.getlist('CLASS', None)[0]
        queryset_sem = queryset_sem.filter(sem_id=sem)
        queryset_class = queryset_class.filter(class_id=cname)
        queryset_subjects = queryset_subjects.filter(sem_id__exact=sem, class_id__class_name__icontains=cname)

    # if 'CLASS' in request.GET:
    #     cname = request.GET['CLASS']
    #     if cname:
    #         flag = 0
    #         queryset_subjects = queryset_subjects.filter(class_id__icontains=cname)
    #
    #
    #
    # if 'SEM' in request.GET:
    #     sem = request.GET['SEM']
    #     if sem:
    #         flag = 0
    #         queryset_subjects = queryset_subjects.filter(sem_id__exact=sem)
    #






    context = {
        'class': queryset_class,
        'sems': queryset_sem,
        'subjects': queryset_subjects,
        'details': queryset_userdetails

    }

    if flag == 1:
        messages.success(request, 'Enter a value')
        return render(request, 'newreval/newrevalhead.html', {})

    else:
        return render(request, 'newreval/newreval.html', context)


def result(request):
    args = {}
    if request.POST:
        args['subjects'] = request.POST.getlist('vehicle', None)
        print(args['subjects'][0])
        for i in range(len(args['subjects'])):
            print(i)
        args['total'] = (i+1)*200
        username = request.user.username
        print(username)
        args['username'] = username
        intuser = User.objects.get(username='shwetha')
        sub=Subjects.objects.get(sub_name = args['subjects'][0])
        p=Reval2(ktu_id=intuser, fees = (i+1)*200, subject=sub)
        p.save()
        a=Reval2.objects.all()
        print(a)
    return render(request, 'newreval/result.html', args)

