# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except 
# para lidar com a divisão por zero, caso a lista esteja vazia.

def calcular_media(lista):
    try:
        # Calcula a média dividindo a soma dos elementos pelo número de elementos
        media = sum(lista) / len(lista)
    except ZeroDivisionError:
        # Lida com a exceção caso a lista esteja vazia
        return "Erro: A lista está vazia. Não é possível calcular a média."
    except TypeError:
        # Lida com a exceção caso os elementos da lista não sejam números
        return "Erro: A lista contém elementos não numéricos."
    else:
        # Retorna a média calculada caso não haja erro
        return media

# Exemplo de uso
lista1 = [10, 20, 30]
lista2 = []
lista3 = [10, "vinte", 30]

print(f"Média da lista1: {calcular_media(lista1)}")  # Deve retornar 20.0
print(f"Média da lista2: {calcular_media(lista2)}")  # Deve retornar erro de lista vazia
print(f"Média da lista3: {calcular_media(lista3)}")  # Deve retornar erro de elementos não numéricos
