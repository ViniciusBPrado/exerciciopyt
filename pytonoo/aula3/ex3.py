# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma = 0

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

for elemento in lista_numeros:
    if elemento % 2 != 0:
        soma += elemento
        

print('A soma dos númerios impares é: ',soma )
