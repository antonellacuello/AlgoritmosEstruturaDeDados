# Exercícios de Strings
# 1) Leia um string e verifique se é um palindromo. Exemplos: ana, ovo, civic, natan, arara.
'''p = input('Digite uma palavra: ')
c = 0
c1 = -1
espelho = ''

while c < len(p):
	espelho += p[c1]
	c += 1
	c1 -= 1

if p == espelho:
	print(f'{p.capitalize()} é um PALINDROMO')
else:
	print(f'{p.capitalize()} NÃO é um palindromo')'''

# 2) Leia uma senha e diga se ela é: FRACA -> 1 tipo; MÉDIA: 2 tipos; FORTE: 3 tipos. Tipos: alfabético, númerico e especial. 
senha = input('Crie uma senha: ')
alf = False
num = False
esp = False
i = 0
while i < len(senha):
	p = ord(senha[i])
	if (p >= 65 and p < 91) or (p >= 97 and p < 123):
		alf = True
	elif p >= 48 and p < 58:
		num = True
	else:
		esp = True
	i += 1

if alf == True and num == False and esp == False:
	print('Senha FRACA. Tente outra.')
elif alf == True and num == True and esp == False:
	print('Senha MÉDIA.')
else:
	print('Senha FORTE')

