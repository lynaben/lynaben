from django.urls import path, include
from . import views
from .views import home, index, search_product,search_product_dop, update_dop



urlpatterns = [
    path('', home, name="home"),
    path('home', home, name="home"),
    path('add', index, name='add'),
    path('search', search_product, name='search'),
    path('search_product_dop', search_product_dop, name='search_product_dop' ),
    path('update_dop/<int:GTIN>/', update_dop, name = 'update_dop'),

]