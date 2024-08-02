# Escreva um programa que mostre a seguinte sequência, tendo informado sua altura e elemento a ser repetido
'''

           1
         2 2 2
       3 3 3 3 3
     4 4 4 4 4 4 4
   5 5 5 5 5 5 5 5 5
   …
   N N N N N N N …
'''  

'''h = int(input('Informe a altura da escadinha: '))
e = input('Do que a escadinha será feita? ')
ch = 1
cspace = h - 1

while ch <= h:
	print((' ' * cspace) + ((e + ' ') * ch))
	ch += 1
	cspace -= 1'''

# prisco
'''altura = int(input('Altura: '))
tijolo = input('Do que será feita a pirâmide: ')
andar = 1
cont = 1
espaço = ' '
desloc = altura - 1

while andar <= altura:
	print((desloc * espaço) + (cont * tijolo))
	andar += 1
	cont += 2
	desloc -= 1'''

# sem usar o recurso do python
altura = int(input('Altura: '))
tijolo = input('Do que será feita a pirâmide: ')
andar = 1
cont = 1
espaco = ' '
desloc = altura - 1

while andar <= altura:
	# print((desloc * espaço) + (cont * tijolo))
	cont2 = 0
	espaco_montado = ''
	while cont2 < desloc:
		espaco_montado = espaco_montado + espaco
		cont2 += 1
		# print(espaco_montado)
	cont2 = 0
	tijolo_montado = ''
	while cont2 < cont:
		tijolo_montado = tijolo_montado + tijolo
		cont2 += 1
	print(espaco_montado + tijolo_montado)
	andar += 1
	cont += 2
	desloc -= 1
