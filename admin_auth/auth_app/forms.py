from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Livre, Auteur, Domaine, Editeur, Classe, ECUE, Exemplaire, Emprunt, Etudiant

# user creation form
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'is_student', 'is_teacher', 'email')

# book creation form
class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ('title', 'isbn', 'publication_date', 'language', 'nb_page', 'prix_unitaire', 'Qte_stock', 'domaine_id')

# auteur creation form
class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ('first_name', 'last_name', 'pays')

# domaine creation form
class DomaineForm(forms.ModelForm):
    class Meta:
        model = Domaine
        fields = ('domaine_name',)

# examplaire creation form
class ExemplaireForm(forms.ModelForm):
    class Meta:
        model = Exemplaire
        fields = ('exemplaire_number', 'edition_number', 'etat', 'disponible', 'livre_id', 'editeur_id')

# editeur creation form
class EditeurForm(forms.ModelForm):
    class Meta:
        model = Editeur
        fields = ('editeur_name', 'pays')

# classe creation formation
class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ('classe_name', 'classe_niveau', 'effectif')

# ecue creation form
class ECUEForm(forms.ModelForm):
    class Meta:
        model = ECUE
        fields = ('ecue_name', 'classe_id')

# emprunt creation form
class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ('date_emprunt', 'delais', 'date_remise', 'etat_remise', 'exemplaire_id', 'user_id')

# etudiant creation from
class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ('matricule', 'user_id', 'classe_id')