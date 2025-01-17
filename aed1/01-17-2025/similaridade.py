#1. Similaridade de strings. Crie uma função que receba 2 strings e retorne a similaridade. Len, letras em comum, letras divergentes, porcentagem de similaridade
# = letras divergentes. útil para ver quando palavras são má escritas. difereça de tamanho, preencher as letras faltantes com espaços. quantas coisas tenho que 
# fazer para uma chegar na outra (retirar ou adicionar letras). resultado 0 ou 1.
def similaridade(str1, str2):
    if len(str1) > len(str2):
        str_maior = list(str1)
        str_menor = list(str2)
    else:
        str_maior = list(str2)
        str_menor = list(str1)

    diferenca = len(str_maior) - len(str_menor)
    i = 0
    while i < diferenca:
        str_menor.append('')
        i += 1

    letras_iguais = 0
    letras_diferentes = 0
    for i, letra in enumerate(str_maior):
        if letra in str_menor:
            letras_iguais += 1
        else:
            letras_diferentes += 1

    return int(100 * letras_iguais / len(str1)), letras_iguais, len(str_maior)


similaridade = similaridade('casa', 'caasa')
print(similaridade)