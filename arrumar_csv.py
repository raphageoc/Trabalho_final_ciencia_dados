

import csv
reader=open('/home/raphael/Downloads/OneDrive-2018-05-17/errado2018-02-01_Despesas_-_Base_de_Dados.csv', 'r')


arquivo = csv.writer(open('/home/raphael/Downloads/OneDrive-2018-05-17/errado2018-02-01_Despesas_-_Base_de_Dados_arrumado1.csv', 'w'))
# reader = csv.reader(f)
string=reader.read().replace('\r\n',';')
string=string.replace(',','.')
reader.close()
dic=string.split(';')
arq = []
tam =[]
cont = 0
string = ""
ini=True

for i in dic:


    if (i == '2017' or i =='2018'):
        ini=True
    else:
        ini=False

    if (ini == True):

        arquivo.writerow((string.split(';')))
        string = ""
        string = string+ ";" + i


    if (ini == False):
        string = string+ ";" + i








# arquivo.write(str(arq))

# t=len(tam)
# cont1=0
# while cont1<t-1:
#
#     if ((tam[cont1+1] -tam[cont1]) != 36):
#         print (tam[cont1+1] -tam[cont1])
#     cont1+=1

# for row in string:
#     # arq.append(str(row))
#     cont=cont+1
#     l = str(row).split(';')
#     # print len(i)
#     # tam.append(len(i))
#
#     if(l[0] != "2017" and l[0] != "2018"  ):
#         print l
#         print "numero da linha"
#         print cont
