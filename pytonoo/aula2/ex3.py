# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e 
# a senha fornecidos correspondem aos valores esperados determinados por você.

nome_de_usuario = str(input('\nDigite seu usuário: '))
senha_de_usuario = int(input('\nDigite sua senha: '))

nome = 'vinicius'
senha = 102030

if nome_de_usuario == nome and senha_de_usuario == senha:
    print("\nOs dados foram preenchidos corretamente")
else:
    print("\nVocê errou os dados de acesso.")