from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from . import models

# Base Template View
#----------------------
class BaseView(TemplateView):

    template_name = 'home.html'

# Ficha Template View
#----------------------
class FichaView(TemplateView):

    template_name = 'ficha.html'

# Classes Template View
#----------------------
class ClassesView(TemplateView):

    template_name = 'classes.html'
    
# Racas Template View
#----------------------
class RacasView(TemplateView):

    template_name = 'racas.html'

# Equipamentos Template View
#----------------------
class EquipamentosView(TemplateView):

    template_name = 'equipamentos.html'

# Magias Template View
#----------------------
class MagiasView(TemplateView):

    template_name = 'magias.html'

# Magias Template View
#----------------------
class FichaCreateView(CreateView):

    model = models.Ficha
    template_name = 'ficha.html'
    success_url = reverse_lazy('gen:ficha')
    fields = ['nome', 'raca', 'classe', 'equipamento']

# Ficha List View
#----------------------
class FichaView(ListView):

    model = models.Ficha
    template_name = 'ficha-listagem.html'