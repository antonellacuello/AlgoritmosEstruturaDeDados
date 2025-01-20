# AULA DE PONTEIROS - 10/01/12025
import sys #biblioteca para usar funções do sistema

#ponteiros são variáveis que apontam para determinado espaço da memória
texto = ['678']
print('Ponteiros -->', sys.getrefcount(texto)) #2 -> sys + texto, pois a biblioteca sys conta como ponteiro e o texto tb
outro = texto
print(texto, id(texto))
print(outro, id(outro))
print('---------')
print('Ponteiros -->', sys.getrefcount(texto)) #sys + texto + outro