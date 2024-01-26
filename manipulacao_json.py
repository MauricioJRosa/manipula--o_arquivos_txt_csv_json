## JavaScript Object Notation
# Ele é estruturado por chaves e valores (dicionario)

# Json é usado para troca de informações entre sistemas backends
# é o formato utilizado pelas APIs
# Graphql as APIs REST

## Capturar uma informação da internet

import urllib.request
import json

url = 'http://api.open-notify.org/astros.json'

## Capturar essas informações em dados JSON

pega_json = urllib.request.urlopen(url).read().decode()

## Converter esses valores em dicionários para manipulação

dic_json = json.loads(pega_json)

## Iterar os valores do dicionário

for c in dic_json.values():
    print(c)

print(dic_json)


for p in dic_json['people']:
    print(p['name'])


## Cria um arquivo json com os valores extraidos
    
with open('arquivos/nomes.json','w+') as f:
    json.dump(dic_json,f,indent=4)


