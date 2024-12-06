# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar 
# se o número é par ou ímpar.

numero = int(input('Insira um número: '))

if numero % 2 == 0:
    print('O número digitado é PAR ')
else:
    print('O número digitado é IMPAR ')