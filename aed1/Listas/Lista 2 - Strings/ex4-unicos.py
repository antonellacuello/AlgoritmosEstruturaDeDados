# 4. Dada uma lista de números inteiros informada pelo usuário, escreva um programa em Python que conte quantos números únicos (diferentes) estão presentes 
# na lista. A digitação dos elementos da lista deve encerrar quando for digitado o número zero.

numeros = [5, 3, 7, 9, 5, 3, 1, 1, 3, 1, 2, 3, 4, 2,4, 6, 3, 7, 9, 5, 3, 6, 6, 7, 1978, 2024, 1000, 2024, 2025]

def numerosUnicos(lista):
    unicos = []
    for numero in lista:
        if numero not in unicos:
            unicos.append(numero)
    return len(unicos)

unicos = numerosUnicos(numeros)
print(f'Existem {unicos} números únicos.')