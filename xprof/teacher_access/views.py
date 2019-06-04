from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404

from .forms import *
from .models import *

# Create your views here.


def check_log(request):
    if 'logged' not in request.session:
        request.session['logged'] = False

    if not (request.session['logged']
            or request.path == '/teacher/auth'
            or request.path == '/admin'
            or request.path == '/teacher/register'):
        return redirect('authentication')
    else:
        return redirect('home')


def log_page(request):
    auth_error = False

    form = AuthForm(request.POST or None)

    if form.is_valid():
        login = form.cleaned_data['login']
        password = form.cleaned_data['password']

        auth_check = Teacher.objects.filter(login=login, password=password)

        if not auth_check.exists():
            auth_error = True
        else:
            request.session['firstname'] = auth_check[0].firstname
            request.session['name'] = auth_check[0].name
            request.session['logged'] = True
            return redirect('home')

    return render(request, 'teacher_access/auth_page.html', locals())


def new_user(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('authentication')

    return render(request, "teacher_access/register.html", locals())


def log_out(request):
    request.session['firstname'] = ''
    request.session['name'] = ''
    request.session['logged'] = False
    return redirect('authentication')


def home_page(request):
    return render(request, 'base.html', {"firstname": request.session['firstname'], "name": request.session['name']})

