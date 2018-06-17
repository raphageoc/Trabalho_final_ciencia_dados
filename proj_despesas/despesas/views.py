# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from despesas.models import Empresas, Despesas
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from despesas.models import Tema
import json
from datetime import datetime


def retorna_geodjango(request):

    opt=request.GET['consulta_tema']
    di=request.GET['d_i']
    df=request.GET['d_f']


    geoj = serialize('geojson', Despesas.objects.filter( data__gt=datetime.strptime(di, '%Y-%m-%d'), data__lt=datetime.strptime(df , '%Y-%m-%d'), ds_funcao=opt ) ,
          geometry_field='geom')


    return HttpResponse(geoj, content_type='json')

def inicial(request):

    t = Tema.objects.values('funcao').distinct()
    temas=[]
    for i in t:
        try:
            print i
            temas.append(str(i['funcao']))
        except Exception as erro:
            print erro

    return render(request, 'despesas/index.html', {'temas': temas})
