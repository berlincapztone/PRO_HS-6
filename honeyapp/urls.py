from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('oil/',  views.oil_page, name='oil_page'),
    path('spices/',views.spices_page, name='spices_page') ,
    path('honey/',views.honey_page, name='honey_page') ,
    path('bulk/',views.bulk_page, name='bulk_page'),
    path('retail/',views.retail_page, name='retail_page'),
    path('honeypro/',views.pro_page, name='pro_page'),
    path('bee/',views.beewax_page, name='bee_page'),
    path('can/',views.candel_page, name='can_page'),
    path('coc/',views.coc_page, name='coc_page')
]