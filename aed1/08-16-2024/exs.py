# Aula de Strings, Listas e Dicionários
# 1. Leia uma string e escreva letra por letra
'''
s = input('Digite algo: ')
c = 0

while c <= len(s):
	print(s[c])
	c += 1
'''

# 2. Leia um nome e escreva apenas as vogais do nome e diga quantas são
'''
nome = input('Digite seu nome: ')
c = 0
vogais = ''
total = 0

while c < len(nome):
	s = nome[c]
	if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
		vogais += s + ', '
		total += 1
	c += 1

print(f'Vogais: {vogais.upper()} \nTotal de vogais: {total}')
'''

# 3. Leia uma palavra e mostre seu espelho. ex: Andre -> Erdna
'''
palavra = input('Digite uma palavra: ')
c = 0
c1 = -1
espelho = ''

while c < len(palavra):
	espelho += palavra[c1]
	c += 1
	c1 -= 1

print(f'O espelho da sua palavra é {espelho.upper()}')
'''
# 3. a) Leia uma música e uma vogal. Escreva a música trocando todas as vogais pela vogal alvo.
'''
musica = 'o sapa nao lava o pe'
vogal = input('Digite uma vogal: ')
c = 0
misici = ''

while c < len(musica):
	p = musica[c]
	if (p == 'a' or p == 'e' or p == 'i' or p == 'o' or p == 'u') and p != vogal:
		misici += vogal
	else:
		misici += musica[c]
	c += 1
	
print(misici)		
'''

# 3. b) Leia um nome e faça o espelho do nome: Antonella Cuello -> allenotna olleuc, não olleuc allenotna

ns = 'antonella manuela cuello'
tamanho = len(ns)
espelho = ''
palavra = ''
c = 0

while c < tamanho:
    if ns[c] == ' ':
        espelho += palavra + ' '
        palavra = ''
    else:
        palavra = ns[c] + palavra
    c += 1

espelho += palavra

print(espelho)

# ns = 'antonella manuela cuello'
# c = 0
# c1 = -1
# espelho = ''
# nome = ''

# while c < len(ns):
# 	espelho += ns[c1]
# 	c += 1
# 	c1 -= 1

# c = 0
# nome2 = ''
# while c < (len(espelho) + 1):
# 	p = espelho[c -1] 
# 	nome += p
# 	if  p == len(espelho):
# 		print('zz')
# 		p = ' '
# 	else: 
# 		p = espelho[c]
# 	if p == ' ':
# 		nome2 = nome + nome2
# 		nome = ''
# 	c += 1
# print(nome2)
# print(p)

'''ns = 'antonella manuela cuello'
c = 1
espelho = ''
while c <= len(ns): 
    espelho += ns[-c] 
    c += 1

c = 0
nome = ''
nome2 = ''
while c <= len(espelho): 
    p = ' '
    if c != len(espelho):
        p = espelho[c] 
    nome += p
    if p == ' ':
        nome2 = nome + nome2
        nome = ''
    c += 1
print(nome2)'''
