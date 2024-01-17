from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, AuteurForm, DomaineForm, EditeurForm, ClasseForm, ECUEForm
from .models import ECUE, Classe


# Create your views here.

# home view
def home(request):
    return render(request, 'home.html')

# signup view or register
def signup(request):
    if request.user.is_authenticated: # if current user is authenticated then redirect to home /
        return redirect('/')
    if request.method == 'POST': # create user via post method
        form = CustomUserCreationForm(request.POST)
        # print("form if:", form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            # print(form)
            return render(request, 'signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        # print("form else:", form)
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
            return redirect('/')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            # print(form)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        # print(form)
        return render(request, 'login.html', {'form': form})

# profile
@login_required(login_url='/signin/')
def profile(request):
    return render(request, 'profile.html')

# create author
def authorCreate(request):
    model_name = 'author'
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        # print("form if:", form)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')  # Redirect to a success page
            except:
                pass
    else:
        form = AuteurForm()
        # print("form else:", form)
    return render(request, 'form_creation.html', {'form': form, 'model_name': model_name})


# create book
def bookCreate(request):
    model_name = 'book'
    return render(request, 'form_creation.html', {'model_name': model_name})

# create domaine
def domaineCreate(request):
    model_name = 'domaine'
    if request.method == 'POST':
        form = DomaineForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')  # Redirect to a success page
            except:
                pass
    else:
        form = DomaineForm()
    return render(request, 'form_creation.html', {'form': form, 'model_name': model_name})

# create examplaire
def examplaireCreate(request):
    model_name = 'examplaire'
    return render(request, 'form_creation.html', {'model_name': model_name})

# create author
def editeurCreate(request):
    model_name = 'editeur'
    if request.method == 'POST':
        form = EditeurForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')  # Redirect to a success page
            except:
                pass
    else:
        form = EditeurForm()
    return render(request, 'form_creation.html', {'form': form, 'model_name': model_name})

# create edition
def editionCreate(request):
    model_name = 'edition'
    return render(request, 'form_creation.html', {'model_name': model_name})

# create emprunt
def empruntCreate(request):
    model_name = 'emprunt'
    return render(request, 'form_creation.html', {'model_name': model_name})

# create remise
def remiseCreate(request):
    model_name = 'remise'
    return render(request, 'form_creation.html', {'model_name': model_name})

# create classe
def classeCreate(request):
    model_name = 'classe'
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')  # Redirect to a success page
            except:
                pass
    else:
        form = ClasseForm()
    return render(request, 'form_creation.html', {'form': form, 'model_name': model_name})

# create ecue
def ecueCreate(request):
    model_name = 'ecue'
    classe_data = Classe.objects.all()
    if request.method == 'POST':
        form = ECUEForm(request.POST)
        if form.is_valid():
            print(form)
            try:
                form.save()
                return redirect('/')  # Redirect to a success page
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(form.errors)
    else:
        form = ECUEForm()
    return render(request, 'form_creation.html', {'form': form, 'model_name': model_name, 'classe': classe_data})
