# -*- coding: utf-8 -*-
import psycopg2
from django.contrib.gis.geos import Point
from django.utils.encoding import smart_str, smart_unicode
import json
import requests
import geocoder
import unirest




##################consulta dos cnpjs das despesas####################### where char_length(cpf_cnpj)=14 or char_length(cpf_cnpj)=13
dados =[]

str_connect=("dbname = 'despesas' user= 'postgres' host= 'localhost' port='5432' password= 'postgres'")
sql = 'select * from empresas2 '
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

    try:
        status = i[2]
        cnpj=i[0]
        if status == None and cnpj != None:

            if len(cnpj)==13:
                cnpj1='0'+cnpj
            else:
                cnpj1=cnpj

            response = unirest.get("https://www.receitaws.com.br/v1/cnpj/%s" % str(cnpj1))
            resposta =  response.body
            #resposta = smart_unicode(resposta)
            # resposta = json.dumps(smart_unicode(resposta))
            #resposta = json.loads(resposta)






            r_search = str(resposta['status'])





            if r_search == 'ERROR':
                sql = ""
                # sql ="" ("UPDATE empresas2 SET nome = 'cnpj_n_encontrado' WHERE cpf_cnpj='%s'" % str(cnpj))
            else:
                rua = resposta['logradouro']
                numero = resposta['numero']
                cidade = resposta['municipio']
                nome = str(resposta['nome']).replace("'"," ")

                endereco = rua + ',' + numero + '-'+ cidade

                ############################geocodificar com google ####################
                url = 'https://maps.googleapis.com/maps/api/geocode/json'
                params = {'sensor': 'false', 'key':'AIzaSyCH2CpDbw2_Y2fNZ8kQ4t5_-YzuopAlW_Y','address': endereco}
                # AIzaSyCH2CpDbw2_Y2fNZ8kQ4t5_-YzuopAlW_Y
                # AIzaSyCvroGGooqKgub4fzNxq99W1L8FQsUDzVU
                # AIzaSyC7XvrrhmVlEiCL0vCgIoKRYsKbom99a6E ja usasda
                r = requests.get(url, params=params)
                results = r.json()['results']

                if results == []:
                    sql = ("UPDATE empresas2 SET nome = 'cnpj_n_encontrado' WHERE cpf_cnpj like '%s'" % str(cnpj))
                else:
                    location = results[0]['geometry']['location']
                    lat = location['lat']
                    long = location['lng']
                    pnt = Point(float(long), float(lat))
                    sql = (("UPDATE empresas2 SET geom = ST_GeomFromText('POINT(%f %f)',4326), nome='%s' WHERE cpf_cnpj = '%s'") % (float(long),float(lat),nome,str(cnpj)))

            conn = psycopg2.connect(str_connect)
            cur = conn.cursor()
            cur.execute(sql)
            cur.close()
            conn.commit()
            conn.close()
    except Exception as inst:
        print inst
        pass
