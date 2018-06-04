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
sql = 'select * from empresas2 where char_length(cpf_cnpj)=14 order by cpf_cnpj desc'
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

    status = i[2]
    cnpj=i[0]
    if status == None and cnpj != None:

        if len(cnpj)==13:
            cnpj1='0'+cnpj
        else:
            cnpj1=cnpj

        response = unirest.get("https://www.receitaws.com.br/v1/cnpj/%s" % str(cnpj1))
        resposta =  response.body

        # resposta = smart_unicode(resposta)
        # resposta = json.dumps(smart_unicode(resposta))
        print resposta['logradouro']

        rua = resposta['logradouro']
        numero = resposta['numero']
        cidade = resposta['municipio']
