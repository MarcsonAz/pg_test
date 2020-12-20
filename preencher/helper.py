# imports
import datetime
import urllib
import json
import random as rd
file = open('./summary.json')

#funcoes internas do helper
def country_slug(countries):
    saida = []
    for name in countries:
        saida.append(name['Slug'])
    return saida

#def get_country(dictOfNames):
    # pegar obj referente ao pais passado como parametro


#def country_data(country_name, data):
# retornar uma lista/dict com dados para inputar no banco

# variaveis
data = json.load(file)
SQL = "insert into covid19onlinebeta (country,confirmed,deaths,recovered,datetime_data) values(%s, %s, %s, %s, %s)"
countries = country_slug(data['Countries'])
teste = range(20)

#funcoes

# criar dados
def new_data():
    # gerar dados para as variaveis
    #country = countries[rd.randrange(1,10)]
    #obj = country_data(country,data)
    
    # preencher com variaveis
    country = 'Canada'
    confirmed = 100
    deaths = 5
    recovered = 50
    datetime_data = datetime.datetime('2020','3','10')
    
    return (country,confirmed,deaths,recovered,datetime_data)




"""
importado do write para sqlite

def to_tuple(country_list):
    data = []
    for dic in country_list:
        saida = ( dic['country'], dic['date'], dic['confirmed'], dic['deaths'] )
        data.append(saida)
    return data

def to_tuple(country_list):
    data = []
    for dic in country_list:
        saida = ( dic['country'], dic['date'], dic['confirmed'], dic['deaths'] )
        data.append(saida)
    return data

Ler base_banco.json
preencher banco do DJANGO - djangoCovid sqlite

file = open('./summary.json')
data = json.load(file)
data = to_tuple(data)

conn = sqlite3.connect('C:\\mark\\django\\projetos\\djangoCovid\\djangocovidrest\\db.sqlite3')

with conn:
    c = conn.cursor()
    c.executemany('INSERT INTO apiapp_countrytable(country,date,confirmed,deaths) VALUES (?,?,?,?)', data)
    conn.commit()

conn.close()

file.close()
"""