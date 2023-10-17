import json

dicionario1 = {'codigo': 123, 'nome': 'Rodrigo', 'idade': 19}

dicionario2 = {'codigo': 543, 'nome': 'Jonas', 'idade': 56}

lista = [dicionario2,dicionario1]

print(lista)

with open('dados.json', 'w') as arquivo:
    json.dump(lista, arquivo, indent=4, sort_keys=True)