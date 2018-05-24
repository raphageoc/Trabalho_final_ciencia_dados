# -*- coding: utf-8 -*-
import psycopg2
from django.contrib.gis.geos import Point
import json
import requests
import geocoder
import unirest

##################consulta dos cnpjs das despesas#######################
dados =[]

str_connect=("dbname = 'despesas' user= 'postgres' host= 'localhost' port='5432' password= 'postgres'")

sql = 'select * from empresas where char_length(cpf_cnpj)=13 or char_length(cpf_cnpj)=14'
try:
        conn = psycopg2.connect(str_connect)
        cur = conn.cursor()
        cur.execute(sql)
        if (cur.rowcount == 0):
            dados=0
        else:
            dados= cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
except:
        print "I  am unable to connect to the database"

#################################consultando na receitaws o endereco do cnpj

for i in dados:
    import unirest
    cnpj=i[0]
    if len(cnpj)==13:
        cnpj='0'+cnpj
    print cnpj



response = unirest.get("https://www.receitaws.com.br/v1/cnpj/%i" % cnpj)
resposta = response.body

if resposta['status'] == 'ERROR':
    print "cnpj nao encontrado"




else:

    rua = resposta['logradouro']
    numero = resposta['numero']
    cidade = resposta['municipio']
    print resposta
    endereco = rua + ',' + numero + '-'+ cidade
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'key':'AIzaSyC7XvrrhmVlEiCL0vCgIoKRYsKbom99a6E','address': endereco}
    r = requests.get(url, params=params)
    results = r.json()['results']

    results = r.json()['results']
    if results == []:
        print 'nao foi encotrado'
    location = results[0]['geometry']['location']
    print location['lat']
    print location['lng']
    pnt = Point(float(lo), float(la))
