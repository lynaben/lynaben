from django.shortcuts import render, redirect
from produit.models import Produit
from .forms import ProdiutsForm




"""
Fonction qui permet d'afficher la liste des produits
presents dans notre base de données dans notre page 
d'acceuil.
"""
def home(request):
    produits = Produit.objects.all()
    context = {'produits' : produits}
    return render(request, 'home.html', context)


"""
Fonction qui gere l'ajout d'un nouveau produit dans notre base de données 
et elle verifie sa validation avant de l'ajouter.
"""
def index(request):
    if request.method == "POST":
        form = ProdiutsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else :
        form = ProdiutsForm()

    return render(request, 'add.html', {'form' : form})




"""
Fonction qui permet de faire une recherche d'un produit dans notre base de données 
en tappant sur la barre de rechercher le GTIN du produit voulu, si ce dernier existe pas un message
sera renvoyer en disant produit non trouvé, sinon on renvoie le nom et la date de peremption.
"""
def search_product(request):
    if request.method == 'POST':
        query_gtin = request.POST.get('GTIN', None)
        if query_gtin :
            result = Produit.objects.filter(GTIN=query_gtin)
            if len(result) != 0:
                return render(request, 'search_page.html', {'result' : result[0]})

    return render(request, 'search_page.html', {'result' : None})




"""
Fonction qui permet de renvoyer tous les produits a qui sa dOP correspend a la date de peremption rentrer
sur la barre de recherche.
"""
def search_product_dop(request):
    if request.method == 'POST':
        query_date = request.POST.get('DOP', None)
        if query_date :
            result2 = Produit.objects.filter(DOP=query_date)
        if len(result2) != 0:
            return render(request, 'search_product_dop.html', {'result2' : result2[0]})
    return render(request, 'search_product_dop.html', {'result2' : None})





"""
Fonction qui permet de mettre a jour un produit.
"""
def update_dop(request, GTIN):

    post = Produit.objects.get(GTIN = GTIN)
    if request.method == "POST":
        form = ProdiutsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return render(request,'base.html')
    else:
        form = ProdiutsForm(instance=post)

    context = {
        'form': form,
    }
    return render(request, "update_dop.html", context)


    
