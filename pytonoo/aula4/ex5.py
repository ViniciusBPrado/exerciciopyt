# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.


frase = "O rato roeu a roupa do rei de roma e depois teve que dar três pratos de trigo para três tigres tristes! "

frequencia = {}

palavras = frase.split()

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

# Exibir o dicionário com a frequência das palavras
print(frequencia)