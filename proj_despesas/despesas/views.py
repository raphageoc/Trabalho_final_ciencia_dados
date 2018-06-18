# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from despesas.models import Empresas, Despesas, Consulta
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from despesas.models import Tema
from django.db.models import Sum

import json
from datetime import datetime


def retorna_geodjango(request):

    opt=request.GET['consulta_tema']
    di=request.GET['d_i']
    df=request.GET['d_f']

    # geoj = serialize('geojson', json.dumps(Despesas.objects.filter( data__gt=datetime.strptime(di, '%Y-%m-%d'), data__lt=datetime.strptime(df , '%Y-%m-%d'), ds_funcao=opt ).values('nome_empresa','cpf_cnpj','valor','geom').annotate(Sum('valor')), ensure_ascii=False) )
    # # sql =("SELECT nome_empresa, cpf_cnpj as id, sum(valor) FROM despesas where ds_funcao = '%s' group by cpf_cnpj, nome_empresa;" % ('SANEAMENTO'))
    # sql ="SELECT nome_empresa, cpf_cnpj AS id FROM despesas where ds_funcao ='SAUDE' "
    # geoj = serialize('geojson', Despesas.objects.raw(sql),fields=('geom',))

    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("drop table IF EXISTS consulta ;")
    cursor.execute("create table consulta as select cpf_cnpj as id,cpf_cnpj , geom, nome_empresa, sum(valor) from despesas where valor is not NULL and ds_funcao = '%s' and data >= '%s' and data >= '%s' group by cpf_cnpj, nome_empresa,geom" % (opt,di,df))
    cursor.execute("ALTER TABLE consulta ADD COLUMN max float ;")
    cursor.execute("ALTER TABLE consulta ADD COLUMN min float ;")
    cursor.execute("select max(sum),min(sum) from consulta")
    ma=cursor.fetchone()
    print ma[1]
    # mi=cursor.fetchone()[1]


    cursor.execute("update consulta set max = %i, min = %i " % (ma[0],ma[1]))


    geoj = serialize('geojson', Consulta.objects.all())
    # print geoj
    # geoj = serialize('geojson',geoj)




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
