# 2 - Utilizando o dicionário criado no item 1:

#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.

pessoa = [{'nome':'Pedro', 'idade': 20, 'cidade': 'campinas'},
          {'nome':'Lucas', 'idade': 29, 'cidade': 'sumare'},
          {'nome':'Toni', 'idade': 18, 'cidade': 'hortolandia'},
          ]

pessoa[0]['idade'] = 29
pessoa[0]['profissao'] = 'Desenvolvedor'
del pessoa[0]['cidade']

print(f'{pessoa[0]}')