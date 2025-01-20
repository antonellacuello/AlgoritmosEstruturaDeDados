# Aula de Strings -> 06/09/2024
# EXEMPLO 1) Colocar a primeira letra de cada nome em MAIUSCULO e o restante em MINUSCULO

nome = 'anDRe prisco VARGAS'
print(nome.lower())
print(nome.upper())
print(nome.capitalize()) #apenas a primeira letra em M
ls_nome = nome.split(' ') # SPLIT - divide strings em partes, cria uma lista com elas e separa
print(ls_nome) # ['AnDRé', 'prisco', 'VARGAS']

if 'prisco' in ls_nome:  
	print('tem')
else:
	print('não tem')

preposicao = ['de', 'da', 'dos', 'das', 'e']
# jeito dificil
'''novo_nome = ''
for um_nome in ls_nome:  #pega cada nome
	codigo = ord(um_nome[0]) 
	if codigo >= ord('a') and codigo <= ord('z'): # se for m
		novo_nome = novo_nome + chr(codigo - 32)
	else:
		novo_nome = novo_nome + um_nome[0]  #se já for M
	i = 1  #começa no 1 pq a letra na posição 0 'transformanda em M
	while i < len(um_nome):  #pega cada caracter
		codigo = ord(um_nome[i])
		if codigo >= ord('A') and codigo <= ord('Z'):
			novo_nome = novo_nome + chr(codigo + 32)
		else:
			novo_nome = novo_nome + um_nome[i]
		i += 1
	novo_nome += ' '
print(novo_nome)'''

# jeito mais simples
novo_nome = ''
for um_nome in ls_nome:  #pega cada nome
	if um_nome in preposicao:
		novo_nome = novo_nome + um_nome
	else:
		novo_nome = novo_nome + um_nome[0].upper()
		i = 1  
		while i < len(um_nome):  
			novo_nome = novo_nome + um_nome[i].lower()
			i += 1
	novo_nome += ' '
print(novo_nome)


