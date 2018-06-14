# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from despesas.models import Empresas
from django.shortcuts import render
from django.core.serializers import serialize
import json

def inicial(request):

    # q = Empresas.objects.values('cpf_cnpj').distinct()
    # q =Empresas.objects.all()
    # for i in q:
    #     print i
    geoj = serialize('geojson', Empresas.objects.all(),
          geometry_field='geom'
          )
    # print geoj
    # geoj = json.dumps(geoj, ensure_ascii=True, encoding='utf-8')
    return render(request, 'despesas/index.html', {'geo': geoj})
