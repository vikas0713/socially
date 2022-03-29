from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from timeline.models import Post


def login_user(request):
    if request.method == 'POST':
        username, password = request.POST.get("username"), request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')


@login_required
def index(request):
    return render(request, 'index.html', {"all_posts": Post.objects.all().order_by('id')})
