from django.urls import path
from apps.catalogs.views import empresas_list, notafiscal_list, empresas_notas_list, popula_sql, home_list

urlpatterns = [
    path('', home_list, name = 'home-list'),
    path('empresas/', empresas_list, name = 'empresas-list'),
    path('notafiscal/', empresas_notas_list, name = 'notafiscal-detail'),
    path('notafiscal/<pk>/', notafiscal_list, name = 'notafiscal-detail'),
    path('populasql/', popula_sql, name = 'popula-sql')
]