# Mostrar a tabuada de um número

t = int(input('Digite o número da tabuada que você deseja visualizar: '))
c = 0
r = 0
print(f'\nTABUADA DO {t} \n')

while c <= 10:
	r = c * t
	c += 1
	print(f'{c} X {t} = {r}')
