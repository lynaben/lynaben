from django.db import models

# Create your models here.

class Produit(models.Model) :

    """
    Classe qui represente un objet de type produit pour pouvoir le modeliser avec 
    un GTIN (code barre), un nom, une marque, une date de fabrication (DOM) 
    et une date de peremption et une quantité et un prix.
    """
    GTIN = models.BigIntegerField(primary_key = True,null = False)
    name = models.CharField(max_length = 255,null = True)
    mark = models.CharField(max_length = 255,null = True)
    DOM = models.DateField(null = True)
    DOP = models.DateField(null = True)
    quantity = models.IntegerField(null = True)
    price = models.FloatField(null = True)

    def __str__(self):
        return self.name






    
