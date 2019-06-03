from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404

from .forms import *
from .models import *

# Create your views here.


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
            return redirect('home')

    return render(request, 'teacher_access/auth_page.html', locals())


def home_page(request):
    print(request.session["name"])
    return render(request, 'base.html', {"firstname": request.session['firstname'], "name": request.session['name']})
