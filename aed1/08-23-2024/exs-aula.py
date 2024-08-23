# Aula de Strings: EXERCÍCIOS
# Tabela ASCII
'''c = 0 
while c < 300:
	print(c, chr(c))
	c += 1'''
# A função ord() recebe uma string de tamanho igual à uma unidade e retorna o Unicode equivalente ao argumento fornecido. Em outras palavras, dado uma string de tamanho 1, a função retorna um número inteiro (integer, "int()") representado o código Unicode. A função chr() é responsável pela operação inversa à realizada pela função ord(). Ou seja, ela recebe uma integer e retorna uma string equivalente ao código Unicode fornecido.

# 1. Capitalizar um nome
'''nome = input('Digite seu nome completo: ')
c = 1
tamanho = len(nome)
cap = nome[0].upper()			

while c < tamanho:
	if nome[c] == ' ':
		if nome[c + 1] == 'd' and nome[c + 2] == 'e' and nome[c + 3] == ' ':
			cap = cap + ' de'
			c += 2
		else:
			cap = cap + ' ' + nome[c + 1].upper()
			c += 1
	else:
		cap = cap + nome[c]
	c += 1
print(cap)
'''
# 2. Ler um nome e mostrar um por um
'''nome = input('Digite seu nome completo: ')
c = 0 
nome1 = ''
tamanho = len(nome)

while c < tamanho:
	if nome[c] == ' ':
		print(nome1)
		nome1 = ''
	else:
		nome1 = nome1 + nome[c]
	c += 1
if len(nome1) > 0:
	print(nome1)
'''
# 3. Leia um nome e coloque todas as letras em minusculas
'''nome = input('Digite um nome em letras maiúsculas: ')
c = 0
nome_minusculo = ''

while c < len(nome):
	letra = nome[c]
	codigo = ord(letra)
	if letra == ' ':
		nome_minusculo = nome_minusculo + ' '
	else:
		minusculo = codigo + 32
		nome_minusculo = nome_minusculo + chr(minusculo)
	c += 1
print(nome_minusculo)
'''
# 4. Leia um nome e coloque todas as letras em MAIUSCULAS
'''nome = input('Digite um nome em letras minúsculas: ')
c = 0
nome_maiusculo = ''
while c < len(nome):
	letra = nome[c]
	codigo = ord(letra)
	if letra == ' ':
		nome_maiusculo = nome_maiusculo + ' '
	else:
		maiuscula = codigo - 32
		nome_maiusculo = nome_maiusculo + chr(maiuscula) 
		# print(codigo, letra)
	c += 1
print(nome_maiusculo)'''
