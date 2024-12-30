from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from .forms import RegisterForm, LoginForm 

def home(request):
    return HttpResponse("<h1> Use 'register/' in url to access the site. <h1>")

def in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            viewer_group, created = Group.objects.get_or_create(name='Viewer')
            user.groups.add(viewer_group)
            return redirect('login')
    else: 
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid(): 
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else: 
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    if in_group(request.user, 'Admin'):
        return render(request, 'admin_dashboard.html')
    elif in_group(request.user, 'Editor'):
        return render(request, 'editor_dashboard.html')
    else: 
        return render(request, 'viewer_dashboard.html')
    
@user_passes_test(lambda u: in_group(u, 'Admin'))
def admin_only_view(request):
    return render(request, 'admin_only.html')