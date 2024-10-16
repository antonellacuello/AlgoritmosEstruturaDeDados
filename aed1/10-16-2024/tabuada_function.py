def tabuada(num):
	saida = ''
	for i in range(11):
		mult = num * i
		saida = saida + f'{num} x {i} = {mult}\n'
	return saida

# num = int(input('num: '))
# print(tabuada(num))

for i in range(11):
	print(f'TABUADA DO {i}')
	print(tabuada(i)) 

