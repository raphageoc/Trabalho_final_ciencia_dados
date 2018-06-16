# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from despesas.models import Empresas
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from despesas.models import Tema
import json

def inicial(request):

    t = Tema.objects.values('funcao').distinct()
    temas=[]
    for i in t:
        try:

            temas.append(str(i['funcao']))
        except Exception as erro:
            print erro
    # print temas

    # print geoj
    # geoj = json.dumps(geoj, ensure_ascii=True, encoding='utf-8')
    return render(request, 'despesas/index.html', {'temas': temas})

def retorna_geodjango (request):

    la=request.GET['lt']
    lo=request.GET['lg']
    pnt = Point(float(lo), float(la))
    query = AmericaDoSul.objects.get(geom__intersects=pnt)


    geoj = serialize('geojson', Empresas.objects.all(),
          geometry_field='geom'
          )


    return HttpResponse(query.cntry_name)
