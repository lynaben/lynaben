from django.forms import ModelForm
from produit.models import Produit


class ProdiutsForm(ModelForm):

    class Meta: 
        model = Produit
        fields =['GTIN','name', 'mark', 'DOM', 'DOP', 'quantity', 'price' ]