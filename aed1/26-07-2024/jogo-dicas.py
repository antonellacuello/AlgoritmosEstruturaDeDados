# joguinho de dica: quando a pessoa errar 2 vezes, uma dica terá que ser printada e assim por diante (mpinimo de 4 dicas).

'''resposta = 'jungkook'
c = 2

print('----- Adivinhe a resposta! -----\n')
tentativa = input('Insira sua tentativa: ')

while tentativa != resposta:
	tentativa = input('Insira sua tentativa: ')
	c += 1 
	if c == 3:
		print('\nDICA 1: Homem')
	if c == 4:
		print('\nDICA 2: Músico')
	if c == 5:
		print('\nDICA 3: Ásiatico')
	if c == 6:
		print('\nDICA 4: Faz parte do BTS')
	if c >= 7:
		print('\nDICA FINAL: É o mais novo')
	
print(' \nParabéns, você acertou!')'''

# com número limite de tentativas
resposta = 'lola'
c = 2

print('----- Adivinhe a resposta! -----\n')
tentativa = input('Insira sua primeira tentativa: ')

while c <= 10:
	if tentativa == resposta:
		print('Parabéns, você acertou!')
		break
	else:
		if c == 10:
			print('\nCuidado, é sua última chance...')
		tentativa = input('Insira sua nova tentativa: ')
		c += 1
	if c == 3:
		print('\nDICA 1: Um amor meu')
	if c == 4:
		print('\nDICA 2: Do sexo feminino')
	if c == 5:
		print('\nDICA 3: Melhor que seres humanos')
	if c == 6:
		print('\nDICA 4: Tem 5 anos')
	if c == 7:
		print('\nDICA FINAL: É única')
		
if c >= 10 and tentativa != resposta:	
	print(' \nErrou tudo :(')
else:
	print('Parabéns, você acertou!')
		
