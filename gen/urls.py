from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views as gen

app_name = "gen"

urlpatterns = [

    path('', gen.BaseView.as_view(), name='home'),
    path('ficha/criar/', gen.FichaCreateView.as_view(), name='ficha'),
    path('fichas/', gen.FichaView.as_view(), name='fichas'),
    path('classes/', gen.ClassesView.as_view(), name='classes'),
    path('racas/', gen.RacasView.as_view(), name='racas'),
    path('equipamentos/', gen.EquipamentosView.as_view(), name='equipamentos'),
    path('magias/', gen.MagiasView.as_view(), name='magias'),
]