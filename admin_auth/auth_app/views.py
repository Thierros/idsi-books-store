from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# home view
def home(request):
    return render(request, 'home.html')

# signup view or register
def signup(request):
    if request.user.is_authenticated: # if current user is authenticated then redirect to home /
        return redirect('/')
    if request.method == 'POST': # create user via post method
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

# signout or logout
def signout(request):
    logout(request)
    return redirect('/')

# signin or login
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/profile')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

# profile
@login_required(login_url='/signin/')
def profile(request):
    return render(request, 'profile.html')