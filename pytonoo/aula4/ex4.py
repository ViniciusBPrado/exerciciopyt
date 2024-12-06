# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

cidade = [{'nome': 'campinas', 'estado': 'Sao Paulo', 'pais': 'Brasil'}]

if 'estado' in cidade[0]:
    print('A chave "estado" existe! ')
else:
    print('A chave "estado" não existe. ')

if 'populacao' in cidade[0]:
    print("A chave 'populacao' existe! ")
else:
    print("A chave 'populacao' não existe. ")