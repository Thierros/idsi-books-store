from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import os

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Auteur(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)

class Domaine(models.Model):
    domaine_id = models.AutoField(primary_key=True)
    domaine_name = models.CharField(max_length=255)

# filee name function
# def filepath(request, filename):
#     old_filename = filename
#     time_now = datetime.now().strftime("%Y%m%d%H:%M:%S")
#     filename = "%s%s"%(time_now,old_filename)
#     return os.path.join("media/livre_images/", filename)

class Livre(models.Model):
    livre_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20)
    publication_date = models.DateField()
    language = models.CharField(max_length=50)
    nb_page = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    Qte_stock = models.IntegerField()
    domaine_id = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='livre_images/', blank=True, null=True)
    auteurs = models.ManyToManyField(Auteur, through='LivreAuteur')

class LivreAuteur(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)

class Editeur(models.Model):
    editeur_id = models.AutoField(primary_key=True)
    editeur_name = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)

class Classe(models.Model):
    classe_id = models.AutoField(primary_key=True)
    classe_name = models.CharField(max_length=255)
    classe_niveau = models.CharField(max_length=50)
    effectif = models.IntegerField()

class ECUE(models.Model):
    ecue_id = models.AutoField(primary_key=True)
    ecue_name = models.CharField(max_length=255)
    classe_id = models.ForeignKey(Classe, on_delete=models.CASCADE)

class LivreECUE(models.Model):
    livre_id = models.ForeignKey(Livre, on_delete=models.CASCADE)
    ecue_id = models.ForeignKey(ECUE, on_delete=models.CASCADE)

class Exemplaire(models.Model):
    exemplaire_id = models.AutoField(primary_key=True)
    exemplaire_number = models.IntegerField()
    edition_number = models.IntegerField()
    etat = models.CharField(max_length=255)
    disponible = models.BooleanField(default=True)
    livre_id = models.ForeignKey(Livre, on_delete=models.CASCADE)
    editeur_id = models.ForeignKey(Editeur, on_delete=models.CASCADE)

class Emprunt(models.Model):
    emprunt_id = models.AutoField(primary_key=True)
    date_emprunt = models.DateTimeField()
    delais = models.IntegerField()
    date_remise = models.DateTimeField()
    etat_remise = models.CharField(max_length=255)
    exemplaire_id = models.ForeignKey(Exemplaire, on_delete=models.CASCADE)
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     is_student = models.BooleanField(default=False)

class Etudiant(models.Model):
    matricule = models.CharField(primary_key=True, max_length=20)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classe_id = models.ForeignKey(Classe, on_delete=models.CASCADE)