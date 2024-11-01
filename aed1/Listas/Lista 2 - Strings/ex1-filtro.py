# 1. Escreva um programa que leia uma lista de palavras do usuário e retorne outra lista contendo apenas as palavras com mais de 5 caracteres.
def filtra(lista):
    saida = []
    for item in lista:
        if len(item) > 5:
            saida.append(item)
    return saida

segue = True
lista_entrada = ['Antonella', 'aaa', 'bbbbbbbbb']
while segue:
    nome = input('Insira nomes a lista: ')
    if item == '':
        segue = False
    else:
        lista_entrada.append(nome)

lista_saida = filtra(lista_entrada)

print(lista_saida)
