"""
URL configuration for admin_auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auth_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('create/author/', views.authorCreate, name='author_creation'),
    path('create/book/', views.bookCreate, name='book_creation'),
    path('create/domaine/', views.domaineCreate, name='domaine_creation'),
    path('create/examplaire/', views.examplaireCreate, name='examplaire_creation'),
    path('create/editeur/', views.editeurCreate, name='editeur_creation'),
    path('create/edition/', views.editionCreate, name='edition_creation'),
    path('create/emprunt/', views.empruntCreate, name='emprunt_creation'),
    path('create/remise/', views.remiseCreate, name='remise_creation'),
    path('create/classe/', views.classeCreate, name='classe_creation'),
    path('create/ecue/', views.ecueCreate, name='ecue_creation'),
    path('show/book/', views.show_livre,name='show_livre')
    # path('create/student/', views.studentCreate, name='student_creation')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    