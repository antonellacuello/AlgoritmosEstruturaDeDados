# Escreva um código que mostre todas as tabuadas até o número fornecido pelo usuário

t = int(input('Digite até qual tabuada você deseja visualizar: '))
c1 = 1
t1 = 1

while c1 <= t:
	c = 1
	r = 0
	print(f'\nTABUADA DO {t1} \n')

	while c <= 10:
		r = c * t1
		print(f'{c} X {t1} = {r}')
		c += 1
	c1 += 1
	t1 += 1
