from django.shortcuts import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout, models
from django.db.models import Q
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def connexion(request):
    error = False
    # next = request.GET["next"]
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(accueil)
                # return redirect(next)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'login.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def book_attrs(books, page):
    try:
        slide1 = books[0]
        slides = books[1:3]
    except IndexError:
        slide1 = None
        slides = None
    pages = Paginator(books, 20, orphans=8)
    page_content = pages.page(page)
    pagination = pages.page_range
    nom_app = "Livres"
    return (nom_app, slide1, slides, pages, page_content, pagination)

def books(request, page=1):
    books = Livre.objects.all()
    accueil = True
    nom_app, slide1, slides, pages, page_content, pagination = book_attrs(books, page)
    return render(request, "library_content.html", locals())

def books_by_auteur(request, auteur, page):
    books = Livre.objects.filter(id=auteur)
    accueil = False
    nom_app, slide1, slides, pages, page_content, pagination = book_attrs(books, page)
    return render(request, "home.html", locals())
    
def books_by_maison(request, maison, page):
    books = Livre.objects.filter(maison = maison)
    accueil = False
    nom_app, slide1, slides, pages, page_content, pagination = book_attrs(books, page)
    return render(request, "home.html", locals())
    
def books_by_categorie(request, categorie, page):
    categorie = Categorie.objects.get(categorie=categorie)
    books = Livre.objects.filter(categorie=categorie)
    accueil = False
    nom_app, slide1, slides, pages, page_content, pagination = book_attrs(books, page)
    return render(request, "home.html", locals())
    
def books_by_annee(request, annee, page):
    books = Livre.objects.filter(annee=annee)
    accueil = False
    nom_app, slide1, slides, pages, page_content, pagination = book_attrs(books, page)
    return render(request, "home.html", locals())

def book(request, slug):
    book = Livre.objects.get(slug=slug)
    lasts = Livre.objects.filter(owner=book.owner)[:3]
    return render(request, "library_detail.html", locals())

@login_required(redirect_field_name='login')
def ajouter(request, slug=None):
    page = "ADD BOOK"
    url = 'add_book'
    if request.method=="POST":
        form = BookForm(request.POST, request.FILES)
        book = form.save(commit=False)
        book.owner = request.user.profil
        book.slug = slugify(book.titre)
        book.save()
        print(book.owner, book.slug)
        return redirect("library")
    form = BookForm()
    return render(request, "book_form.html", locals())

def modifier(request, slug):
    page = "UPDATE BOOK"
    url = 'update_book'
    book = Livre.objects.get(slug=slug)
    if request.method=="POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        form.save()
        return redirect("library")
    form = BookForm(instance=book)
    return render(request, "book_form.html", locals())

def supprimer(request, slug):
    book = Livre.objects.get(slug=slug)
    if book.owner.user == request.user:
        book.delete()
    return redirect("library")