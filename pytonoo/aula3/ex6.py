# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
#  Utilize um bloco try-except para lidar com possíveis exceções.

soma = 0

lista_numero = [0,4,2,1,6,7,9,8,21,54,'bicicleta']

try:
    for elemento in lista_numero:
        soma += int(elemento)

    print(f'A soma dos elementos é : {soma}')        
except:
    print('O valor está errado')



