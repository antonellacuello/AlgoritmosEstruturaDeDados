import random 
random.seed()

'''while True:
	print(random.randint(0,10))'''

# 1. a) Leia duas palavras e escreva se elas sao anagramas
'''str1 = input('Digite a primeira palavra: ')
str2 = input('Digite a segunda palavra: ')
contagem1 = [0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
contagem2 = [0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if len(str1) == len(str2):
	for letra in str1:
		indice = ord(letra) - ord('a')
		contagem1[indice] = contagem1[indice] + 1
	
	for letra in str2:
		indice = ord(letra) - ord('a')
		contagem2[indice] = contagem2[indice] + 1

		anagrama = True
		c = 0
		while anagrama and c < len(contagem1):
			if contagem1[c] != contagem2[c]:
				anagrama = False 
			c += 1
	if anagrama:
		print('É um anagrama!')
	else:
		print('Não é um anagrama!')
else:
	print('Não é um anagrama!')'''

# utilizando apenas uma lista
'''str1 = input('Digite a primeira palavra: ')
str2 = input('Digite a segunda palavra: ')
contagem = [0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if len(str1) == len(str2):
	for letra in str1:
		indice = ord(letra) - ord('a')
		contagem[indice] = contagem[indice] + 1
	
	for letra in str2:
		indice = ord(letra) - ord('a')
		contagem[indice] = contagem[indice] - 1

	if contagem == [0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
		print('É um anagrama!')
	else:
		print('Não é um anagrama!')
else:
	print('Não é um anagrama!')'''

# 1. b) Leia um nome e escreva um anagrama aleatório desse nome
nome = input('Digite seu nome: ')
anagrama = ''
c = 0
tamanho = len(nome)
letra_nome = random.randint(0, tamanho)
posicoes_utilizadas = []
while posicoes_utilizas != []:
	letra_nome = random.randint(0, tamanho)
	posicoes_utilizadas.append(letra_none)
	print(posicoes_utilizadas)
	if ultima_letra == letra_nome:
		letra_nome = random.randint(0, tamanho)
	else:
		anagrama += nome[letra_nome]
	print(anagrama, ultima_letra, letra_nome)
	 
print(anagrama)

'''nome = input('Digite seu nome: ')
anagrama = ''
c = 0
tamanho = len(nome)
letra_nome = random.randint(0, tamanho)

while tamanho != len(anagrama):
	ultima_letra = letra_nome
	letra_nome = random.randint(0, tamanho)
	if ultima_letra == letra_nome:
		letra_nome = random.randint(0, tamanho)
	else:
		anagrama += nome[letra_nome]
	print(anagrama, ultima_letra, letra_nome)
	 
print(anagrama, letra)'''
# 2. a) Gere uma senha forte aleatória. Pergunte ao usuário se quer que tenha números e/ou letras. EX: letras e números ---> os45criP76mhg
