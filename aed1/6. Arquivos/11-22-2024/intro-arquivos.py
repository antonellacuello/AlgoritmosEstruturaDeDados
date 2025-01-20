# AULA DE ARQUIVOS - 22/11/2024 e 06/12/2024

arq = open('poema.txt', 'r')
#arq - ponteiro para o arquivo
#r - read; w - write; a - append

'''texto = arq.read()
print(texto)
print('---------------')
print()'''

print(arq)  # fala as informações do arquivo 
#lista = arq.readlines()   #tranforma em uma lista de linhas
#print(lista)
'''linha = arq.readline()
print(linha)'''

segue = True 
while segue:
    linha = arq.readline()
    print(linha)
    if linha == '':
        segue = False

arq.close()   #serve para fechar o arquivo e liberar memória
