import json

with open('dados.json', 'r') as arquivo:
    lista = json.load(arquivo)

for item in lista:
    if item['nome'] == 'Rodrigo':
        print('Encontrado')