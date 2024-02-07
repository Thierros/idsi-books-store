from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from auth_app.models import *

# Create your views here.
def home(request):
    exemplaire = Exemplaire.objects.count()
    auteur_count = Auteur.objects.count()
    domaine_count = Domaine.objects.count()
    ecue_count = ECUE.objects.count()


    contexte = {"exemplaire": exemplaire, "auteurs": auteur_count ,"ecue": ecue_count, "domaine": domaine_count}
    return render(request, 'index.html', contexte)

def domaine(request):
    return render(request, 'domaine.html')

def livres(request):
    return render(request, 'livres.html')

def auteurs(request):
    return render(request, 'auteurs.html')

def login(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'ecue.html')

def info(request):
    return render(request, 'info.html')
