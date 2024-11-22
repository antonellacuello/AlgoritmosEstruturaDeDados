# AULA DE ARQUIVOS - 22/11/2024

arq = open('poema.txt', 'r')
#arq - ponteiro para o arquivo
#r - read; w - write; a - append

'''texto = arq.read()
print(texto)
print('---------------')
print()'''

lista = arq.readlines()
print(lista)
arq.close()
